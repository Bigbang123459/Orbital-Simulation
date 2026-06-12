# Orbital Simulation 🪐✨
Welcome to my first Physics and Astronomy simulation project. As a Grade 12 student aspiring to become a computer engineer and a researcher in the scientific field, I created this project to combine my passions for coding, mathematics, and space.

<img width="740" height="372" alt="Orbital Simulation Demo" src="https://github.com/user-attachments/assets/85110a25-537d-4bcf-8152-ad51350a295e" />

## 🚀 Key Features & Methodologies

### 1. Physics & Vector Calculation
In this project, I converted the gravitational force from a scalar value to a 3D vector. By using Newton's Law of Universal Gravitation, I calculated the force magnitude and applied the **unit vector method** to define its direction in 3D space:

<img width="101" height="53" alt="Gravitational Force Formula" src="https://github.com/user-attachments/assets/26447276-989e-433f-a62e-3858470fa80a" />

### 2. Trigonometry & Quadrant Ambiguity Resolution
I calculated the orbital angles of each planet relative to the Sun (as well as the relative angle between the Earth and the Moon) by finding the mathematical **argument**. To accurately determine the angle across a full 360-degree rotation, I implemented the **four-quadrant inverse tangent (`atan2`)** method to successfully resolve the **quadrant ambiguity**:

<img width="232" height="96" alt="Atan2 Piecewise Function" src="https://github.com/user-attachments/assets/e5473a26-6659-43aa-afc5-2ae5e9b17e47" />

### 3. Real-Time NASA Data Integration
Instead of using randomized initial values, this simulation fetches and utilizes **real-time ephemeris data directly from NASA's JPL Horizons system** (via `astroquery`). The numerical integration and 3D animations are processed using **NumPy** and visualized with **Matplotlib**.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** NumPy, Matplotlib, Astroquery, Datetime
* **Concepts:** Newtonian Mechanics, Vector Calculus, Computational Physics

---

## 🏃‍♂️ How to Run
1. **Install:**
   ```bash
   pip install numpy matplotlib astroquery
2. **Fetch the latest orbital data from NASA:**
   run astro_data.py
3. **Start the 3D Simulation:**
   run simulation.py
