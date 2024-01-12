# Reward-pytorch
Pytorch implementations of algorithms associated with reward learning, e.g., inverse reinforcement learning, preference-based reinforcement learning, etc.

## Implemented Algorithms

**Inverse Reinforcement Learning**

- [ ] Generative Adversarial Imitation Learning (GAIL) [[arXiv](https://arxiv.org/pdf/1606.03476.pdf)] [[annotated PDF](./docs/irl/GAIL.pdf)] [[official code](https://github.com/openai/imitation)] [[reproduce-env.yaml](./reproduce/irl/gail.yaml)]
- [ ] Learning Robust Rewards with Adversarial Inverse Reinforcement Learning (AIRL) [[arXiv](https://arxiv.org/pdf/1710.11248.pdf)] [[annotated PDF](./docs/irl/AIRL.pdf)] [[official code](https://github.com/justinjfu/inverse_rl)] [[reproduce-env.yaml](./reproduce/irl/airl.yaml)]
- [ ] Discriminator-Actor-Critic: Addressing Sample Inefficiency and Reward Bias in Adversarial Imitation Learning (DAC) [[arXiv](https://arxiv.org/pdf/1809.02925.pdf)] [[annotated PDF](./docs/irl/DAC.pdf)] [[official code](https://github.com/google-research/google-research/tree/master/dac)] [[reproduce-env.yaml](./reproduce/irl/dac.yaml)]
- [ ] Imitation Learning via Off-Policy Distribution Matching (ValueDice) [[arXiv](https://arxiv.org/pdf/1912.05032.pdf)] [[annotated PDF](./docs/irl/ValueDice.pdf)] [[official code](https://github.com/google-research/google-research/tree/master/value_dice)] [[reproduce-env.yaml](./reproduce/irl/valuedice.yaml)]
- [ ] IQ-Learn: Inverse soft-Q Learning for Imitation (IQ-Learn) [[arXiv](https://arxiv.org/pdf/2106.12142.pdf)] [[annotated PDF](./docs/irl/IQ-Learn.pdf)] [[official code](https://github.com/Div99/IQ-Learn)] [[reproduce-env.yaml](./reproduce/irl/iqlearn.yaml)]

**Preference-based Reinforcement Learning**

- [ ] Extrapolating Beyond Suboptimal Demonstrations via Inverse Reinforcement Learning from Observations(TREX) [[arXiv](https://arxiv.org/pdf/1904.06387.pdf)] [[annotated PDF](./docs/preference/TREX.pdf)] [[official code](https://github.com/hiwonjoon/ICML2019-TREX)] [[reproduce-env.yaml](./reproduce/preferemce/trex.yaml)]
- [ ] Better-than-Demonstrator Imitation Learning via Automatically-Ranked Demonstrations (DREX) [[arXiv](https://arxiv.org/pdf/1907.03976.pdf)] [[annotated PDF](./docs/preference/DREX.pdf)] [[official code](https://github.com/dsbrown1331/CoRL2019-DREX)] [[reproduce-env.yaml](./reproduce/preferemce/drex.yaml)]
- [ ] Preference Transformer: Modeling Human Preferences using Transformers for RL (PT) [[arXiv](https://arxiv.org/pdf/2303.00957.pdf)] [[annotated PDF](./docs/preference/PT.pdf)] [[official code](https://github.com/csmile-1006/PreferenceTransformer)] [[reproduce-env.yaml](./reproduce/preferemce/pt.yaml)]
- [ ] Contrastive Preference Learning: Learning from Human Feedback without RL (CPL) [[arXiv](https://arxiv.org/pdf/2310.13639.pdf)] [[annotated PDF](./docs/preference/CPL.pdf)] [[official code](https://github.com/jhejna/cpl)] [[reproduce-env.yaml](./reproduce/preferemce/cpl.yaml)]
- [ ] Inverse Preference Learning: Preference-based RL without a Reward Function (IPL) [[arXiv](https://arxiv.org/pdf/2305.15363.pdf)] [[annotated PDF](./docs/preference/IPL.pdf)] [[official code](https://github.com/jhejna/inverse-preference-learning)] [[reproduce-env.yaml](./reproduce/preferemce/ipl.yaml)]

## Installation

```bash
git clone https://github.com/BepfCp/Reward-pytorch.git
cd Reward-pytorch
pip install -e .
# logger
cd ..
git clone https://github.com/BepfCp/mllogger
cd mllogger
pip install -e .
```

## Run Experiment

```python
python example.py agent=irl/gail env.id=Hopper-v4 dataset=./data/demo/hopper_expert.h5
```

## Acknowledgement

Thanks to the following tutorial, blog and open-source code:

+ ...

