import numpy as np
import matplotlib.pyplot as plt

# Sample data for 3D sine curve plotting
def generate_sine_curve_data(x_range, num_points):
    x = np.linspace(*x_range, num_points)
    y = np.sin(x)
    z = np.cos(x)
    return x, y, z

# Unit tests
import unittest

class TestSineCurvePlotting(unittest.TestCase):
    
    def test_generate_sine_curve_data(self):
        x, y, z = generate_sine_curve_data((0, 10), 100)
        self.assertEqual(len(x), 100)
        self.assertEqual(len(y), 100)
        self.assertEqual(len(z), 100)
        self.assertTrue(np.all(np.isfinite(y)))
        self.assertTrue(np.all(np.isfinite(z)))

    def test_plot_sine_curve(self):
        x, y, z = generate_sine_curve_data((0, 10), 100)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x, y, z)
        plt.close(fig)  # Prevent the plot from displaying during testing

if __name__ == '__main__':
    unittest.main()