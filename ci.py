import wandb

print(f'The version of wandb is {wandb.__version__}')

assert wandb.__version__ == '1.0.0', f'Expected version 1.0.0, got {wandb.__version__}'
