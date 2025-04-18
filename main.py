from V8RandomnessPredictor import V8RandomnessPredictor

sequence = [
  0.0026343227180927187,
  0.2751195310657766,
  0.14987294404396945,
  0.6754760504043595,
  0.4807256393350896
]

expected = [
  0.8186172276830885,
  0.8174175600327118,
  0.040932064250502886,
  0.9073393584690812,
  0.21063266313574736,
  0.7914478886948133,
  0.20343658858523095,
  0.36894889221582394,
  0.0873381477958548,
  0.39515723893697396
]

predictor = V8RandomnessPredictor(sequence)

for i in range(len(expected)):
  prediction = predictor.predict_next()
  correct = prediction == expected[i]
  print({ "correct": correct, "prediction": prediction, "expected": expected[i] })
