import torch
import torch.nn as nn
import torch.optim as optim


x = torch.randn(100, 10)  # 100 samples, 10 features
y = torch.randn(100, 1)   # 100 samples, 1 target

model = nn.sequential(
    nn.Linear(10, 50), # 10 input features, 50 hidden units
    nn.ReLU(),
    nn.Linear(50, 10),   # 50 hidden units, 10 hidden units
    nn.sigmoid(),
    nn.Linear(10, 1),     # 10 hidden units, 1 output
    nn.ReLU()
)

optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(100):
    y_pred = model(x) # Forward pass
    loss = loss_fn(y_pred, y) # Compute loss
    optimizer.zero_grad() # Update gradients to zero
    loss.backward() # Backward pass
    optimizer.step()  # Update weights