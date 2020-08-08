## Clock-Reader

**version** - `1.1.1`

This Software read time from the Clock Images using Convolutions Neural Network.

### Requirements

- **`python`** - `3.7`
- **`keras`** -  `2.4.3`
- **`tensorflow`** -  `2.2.0`

---

### Project Content

| File      | Description |
| :-----------: | :-----------: |
| **clock.ipynb**   | jupyter notebook for running and testing the model     |
| **model.py**   | neural network implementation     |
| **scripts**      | scripts for generating data       |
| **model** | saved model |

---
### Performance

Network was able to read the clock close to 3 mins(average). Following is a snippet showing network reading clock. 

<img src=result/result.png width="450">

---

### References

- Download the [**dataset**](https://www.kaggle.com/shivajbd/analog-clocks) for this project.
- Read this [**blog**](https://towardsdatascience.com/training-neural-net-to-read-clock-time-9473175171e3) to get all detail of this project.

