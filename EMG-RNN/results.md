* NOTE: `...` means Not Recorded.

### NOTE: Version 0 - 3m 24.5s - 50 epochs | 1 LSTM layer + no test_step (NOTE: val was called test here)
* test_acc                    1.0
* test_loss          0.008260570614347382

### NOTE: Version 1 - 6m 56.2s - 50 epochs | 1 LSTM layer + (actual) test_step
* test_acc                    1.0
* test_loss          0.011739273999063741

### NOTE: Version 2 - 6m 23.2s - 50 epochs | 2 LSTM layers
* test_acc                    1.0
* test_loss           0.00910944269881362 | NOTE: Better than version 1

### NOTE: Version 3 - ... - 100 epochs | hidden_dim = 100, max_epochs = 10
* test_acc                    1.0
* test_loss          0.0007921471925718444 | NOTE: Better than version 2

### NOTE: Version 4 - 1m 27.5s - 10 epochs | hidden_dim = 100, max_epochs = 10, 0.1 val & test size -> ((251, 20, 2)(train), (28, 20, 2)(val), (32, 20, 2)(test), (251,), (28,), (32,))
* test_acc                    1.0
* test_loss          0.000614658913036692

### NOTE: Version 4 Take 2 - ... - 10 epochs | Same as take 1
* test_acc                    1.0
* test_loss                 0.001

### NOTE: Version 5 - ... - 10 epochs |
* test_acc                    1.0
* test_loss          0.000614658913036692

### NOTE: Version 6 - ... - 10 epochs | dedicated test_data (i.e. more train & val data) | Proper hyperparam save
* test_acc            0.8399999737739563
* test_loss           1.1150352953752736

### NOTE: Version 7 - ... - 50 epochs | Overfitting on train data
* test_acc             0.800000011920929
* test_loss            1.563018486656947

### NOTE: Version 8 - 2m 35.7s - 20 epochs | Similar to version 6
* test_acc             0.8399999737739563
* test_loss            1.2786047681196941

### NOTE: Version 9 - ... - 10 epochs | num_layers = 3 -> Worse than version 8 / 6
* test_acc             0.7400000095367432
* test_loss            1.8178476405958646

### NOTE: Version 10 - 1m 27.4s - 10 epochs | num_layers = 1, dropout = 0, batch_size = 32 -> Worst so far.
* test_acc             0.5
* test_loss            2.980378066133708

### NOTE: Version 11 - ... - 10 epochs | num_layers = 1, dropout = 0, batch_size = 8 -> Slighly better than version 10
* test_acc             0.5199999809265137
* test_loss            3.505476648770273         

### NOTE: Version 12 - ... - 15 epochs | hidden_dim = 200, num_layers = 2, dropout = 0.2, batch_size = 16, max_epochs = 15 -> Same as version 11
* test_acc            0.5199999809265137
* test_loss           3.5177215408737537

### NOTE: Version 13 - 2m 0.7s - 15 epochs | hidden_dim = 100 -> Near best.
* test_acc            0.8399999737739563
* test_loss           1.2087183453596664

### NOTE: Version 14 - 2m 4.5s - 15 epochs | hidden_dim = 50 -> Slightly worse.
* test_acc            0.7599999904632568
* test_loss           1.4321332859550602

### NOTE: Version 15 - 2m 1.5s - 15 epochs | hidden_dim = 100, minmax-scaled train+val & test data -> Worse than unscaled data.
* test_acc            0.6200000047683716
* test_loss           0.6734148659557104

### NOTE: Version 16 - 2m 8.8s - 15 epochs | robust-scaled train+val & test data -> Slightly better than MinMax-scaled data.
* test_acc            0.6399999856948853
* test_loss           0.6846206948161125

### NOTE: Version 17 - 2m 5.7s - 15 epochs | standard-scaled train+val & test data -> Worst among the scaled ones.
* test_acc            0.5600000023841858
* test_loss           0.7006366237998009

### NOTE: Version 19 - ... - 15 epochs | standard-scaled train+val+test data (single source) -> ...
* test_acc            0.7187
* test_loss           0.5797437669243664

### NOTE: Version 19 - take 2 - ... - 15 epochs | BiDi - robust-scaled train+val+test data (single source) -> ...
* test_acc            0.65625
* test_loss           0.5581224466441199

### NOTE: Version 20 - ... - 15 epochs | un-scaled train+val+test data (single source) -> ...
* test_acc            1.0
* test_loss           0.00013225189536569815

### NOTE: Version 21 - ... - 15 epochs | robust-scaled train+val+test data (single source) -> ...
* test_acc            0.8125
* test_loss           0.5316235115751624

### NOTE: Version 22 - 2m 1.4s - 15 epochs | un-scaled train+val & test data (both sources mixed) + BiDi -> BiDi seems to be irrelevant here, as expected.
* test_acc            0.6909090876579285
* test_loss           1.1283240873408926

### NOTE: Version 23 - 2m 12.8s - 15 epochs | un-scaled train+val & test data (both sources mixed) -> Mixing both datasets (though with the first one having 6 times more data) slightly decreases the perfect accuracy score.
* test_acc            0.9818181991577148
* test_loss           0.03112286892031658

## Optuna optimization - 56m 48.5s
```
Global seed set to 42
((275, 20, 2), (31, 20, 2), (55, 20, 2), (275,), (31,), (55,))
Best trial: FrozenTrial(number=3, state=TrialState.COMPLETE, values=[1.0], datetime_start=datetime.datetime(2023, 4, 18, 2, 41, 50, 324388), datetime_complete=datetime.datetime(2023, 4, 18, 2, 44, 19, 718464), params={'hidden_dim': 42, 'num_layers': 1, 'dropout': 0.010454300823487694, 'learning_rate': 0.05738663557134362, 'batch_size': 8, 'max_epochs': 18}, user_attrs={}, system_attrs={}, intermediate_values={}, distributions={'hidden_dim': IntDistribution(high=128, log=False, low=16, step=1), 'num_layers': IntDistribution(high=3, log=False, low=1, step=1), 'dropout': FloatDistribution(high=0.5, log=False, low=0.0, step=None), 'learning_rate': FloatDistribution(high=0.1, log=True, low=1e-05, step=None), 'batch_size': CategoricalDistribution(choices=(8, 16, 32)), 'max_epochs': IntDistribution(high=30, log=False, low=10, step=1)}, trial_id=3, value=None)

Best test accuracy: 1.0

Best hyperparameters: {'hidden_dim': 42, 'num_layers': 1, 'dropout': 0.010454300823487694, 'learning_rate': 0.05738663557134362, 'batch_size': 8, 'max_epochs': 18}
```
