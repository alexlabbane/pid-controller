# PID Controller
"A proportional–integral–derivative controller (PID controller or three-term controller) is a control loop mechanism employing feedback that is widely used in industrial control systems and a variety of other applications requiring continuously modulated control. A PID controller continuously calculates an error value {\displaystyle e(t)}e(t) as the difference between a desired setpoint (SP) and a measured process variable (PV) and applies a correction based on proportional, integral, and derivative terms (denoted P, I, and D respectively), hence the name."

\- Wikipedia

# Summary
The kRPC mod for Kerbal Space Program is used to remotely control a rocket using Python. The included script uses a PID controller to hover the rocket at a specified altitude. 
For more information on PID controllers, see: [![PID Controller Tutorial by Brian Douglas](https://img.youtube.com/vi/UR0hOmjaHp0/0.jpg)](https://www.youtube.com/watch?v=UR0hOmjaHp0)


## Video
In the video below, the target altitude was set to 700m. With more optimal choices for the constants _k_, _k<sub>i</sub>_, and _k<sub>d</sub>_, the system could stabilize at 700m faster.

[![PID Controller Demo](https://img.youtube.com/vi/JeSpeotUh78/0.jpg)](https://www.youtube.com/watch?v=JeSpeotUh78)

## Plot
Below is a plot of the error (meters) vs time (seconds) for the above video. 
