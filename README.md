## Clock-Reader

**version** - `1.1.1`

This Software read time from the Clock Images using Convolutions Neural Network.

### Requirements

- **`python`** - `3.7`
- **`keras`** -  `2.4.3`
- **`tensorflow`** -  `2.2.0`

Download dataset from [here](https://www.kaggle.com/shivajbd/analog-clocks) for this project.

---

This project contains following files:

| File      | Description |
| :-----------: | :-----------: |
| **scripts/clock_gen.py**      | Script to generate random clock images       |
| **scripts/pre_process.py**      | Script to prepare data       |
| **clock.ipynb**   | jupyter notebook for running and testing the model     |
| **model/clock.model** | saved model |

---

Following is a snippet showing network reading clock. Network was able to read the clock close to 3 mins(average).

<img src=result/result.png width="450">

---

Read [this]() blog for more detail of this project.
