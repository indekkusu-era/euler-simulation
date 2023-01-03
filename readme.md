# Simulation of the Differential Equations using Euler's Numerical Method

This is my really old code since March 2022, and I am interested to study more about it so stay tuned.

## Description

Euler's Numerical Method is the way to discretize the system of differential equations (with initial values) into the discrete-time system. In the system, we assume the system of differential equations is

$$
\begin{cases}
\frac{dx_1}{dt} = f_1(t, x_1, x_2, ..., x_n)\\
\frac{dx_2}{dt} = f_2(t, x_1, x_2, ..., x_n)\\
...\\
\frac{dx_n}{dt} = f_n(t, x_1, x_2, ..., x_n)
\end{cases}
$$

We can then generate the sequences of discrete functions using recursive method:

$$
x_i(t+\Delta t) = x_i(t) + x_i'(t) \Delta t
$$

Where $\Delta t$ is user-defined interval of time (less = more precision)

## Experimentation with SIR Model

**SIR Model** is the mathematical model to simulate the epidemic/pandemic event, for example **COVID-19**. The system of equations are constructed as follows:

$$
\begin{cases}
\frac{dS}{dt} = -\beta S(t) I(t)\\
\frac{dI}{dt} = \beta S(t) I(t) - \gamma I(t)\\
\frac{dR}{dt} = \gamma I(t)\\
S(t) + I(t) + R(t) = 1
\end{cases}
$$

Where

- $S, I, R$ are the proportion of suspectible, infected and recovered compared to the population
- $\beta$ is the infection rate
- $\gamma$ is the recovery rate

We then generate the discrete event from $t = 0$ to $t = 100$ with $\Delta t = 0.01$, $\beta = 0.5$ and $\gamma = 0.3333$ With initial condition of $I(t) = 0.01$. Obtaining the following results:

![](https://cdn.discordapp.com/attachments/546525809440194560/1059665714568507492/sir.png)

## Experimentation with Simple Harmonic Motion

TBA

## To-do List

- [ ] Generalize the euler method for all system of equations
- [ ] Study the stochastic methods in differential equations for SIR model using this approach
