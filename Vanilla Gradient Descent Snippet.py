while True:
  weights_grad=evaluate_gradient (loss_fun, data, weights)
  weights += step_size * weigths_grad # parameter update
