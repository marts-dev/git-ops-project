import wandb

print(f'The version of wandb is {wandb.__version__}')

assert wandb.__version__ == '0.17.2', f'Expected version 0.17.2, got {wandb.__version__}'
