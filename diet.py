# -*- coding: utf-8 -*-

from gurobipy import *

def solve(speisen, kalorien, fett, kosten, minKalorien, maxFett, obst):

  # Gurobi-Modell erzeugen.
  model = Model("Diätenplanung")

  # Problem ist ein Minimierungsproblem.
  model.modelSense = GRB.MINIMIZE

  # Variablen-Dictionary fuer den Kauf anlegen.
  xKaufen = {}
  # Variablen in Gurobi erzeugen und hinzufuegen.
  for speise in speisen:
    xKaufen[speise] = model.addVar(obj = kosten[speise], name = ('x_' + speise))

  # Variablen bekannt machen.
  model.update()

  # Constraint: Mindestmenge an Kalorien.
  model.addConstr(quicksum(kalorien[speise] * xKaufen[speise] for speise in speisen) >= minKalorien)
  
  # TODO: Constraint: Maximalmenge an Fett.
  model.addConstr(quicksum(fett[speise] * xKaufen[speise] for speise in speisen) <= maxFett)

  # Constraint: Ein Drittel der Gesamtmenge muss Obst sein.
  model.addConstr(1.0/3.0 * quicksum(xKaufen[speise] for speise in speisen) <= quicksum(xKaufen[speise] for speise in obst))

  # TODO: Constraint: Maximal 8 Einheiten einer Speise
#  model.addConstr(bool(all([xKaufen[speise] for speise in speisen] <= [8 for i in range(0,8)])))
#  model.addConstr(max_([xKaufen[speise] for speise in speisen], constant = 9) <= 8)
  for speise in speisen:
    model.addConstr(xKaufen[speise] <= 8)
  # Problem loesen lassen.
  model.optimize()

  model.write("model.lp")
  # Ausgabe der Loesung.
  if model.status == GRB.OPTIMAL:
    print(f"\nOptimaler Zielfunktionswert: {model.ObjVal}\n")
    for speise in speisen:
      print(f"Es werden {xKaufen[speise].x} Mengeneinheiten von {speise} gekauft.")
  else:
    print(f"Keine Optimalloesung gefunden. Status: {model.status}")

  return model
