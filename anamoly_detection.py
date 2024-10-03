import numpy as np
import random
import math
import matplotlib.pyplot as plt
from collections import deque


# Simulating the Data Stream
def generate_data_stream():
    """
    This function generates a continuous stream of data with regular patterns,
    random noise, and occasional anomalies.
    """
    t = 0
    while True:
        # Regular pattern: Sine wave + random noise
        regular_value = 10 * math.sin(0.1 * t) + random.uniform(-1, 1)
        
        # Random anomalies (e.g., spikes or dips)
        if random.random() < 0.01:  # 1% chance of an anomaly
            anomaly = random.uniform(20, 30)  # Spike in value
            yield anomaly
        else:
            yield regular_value
        
        t += 1

# Anomaly Detection using Z-Score algorithm
class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        """
        Initializes the anomaly detector with a sliding window size and a Z-score threshold.
        """
        self.window_size = window_size
        self.threshold = threshold
        self.data = deque(maxlen=window_size)
    
    def detect(self, new_value):
        """
        Detects anomalies based on Z-Score. Returns True if an anomaly is detected, else False.
        """
        if len(self.data) < self.window_size:
            self.data.append(new_value)
            return False
        
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        
        # Z-score calculation to detect anomalies
        z_score = (new_value - mean) / std_dev if std_dev > 0 else 0
        
        self.data.append(new_value)
        
        if abs(z_score) > self.threshold:
            return True
        else:
            return False

# Real-time Visualization
def visualize_data(stream, detector):
    """
    Plots the data stream in real time and marks detected anomalies in red.
    """
    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots()
    data_points = []
    anomaly_points = []
    
    for value in stream:
        data_points.append(value)
        is_anomaly = detector.detect(value)
        
        if is_anomaly:
            anomaly_points.append((len(data_points) - 1, value))
        
        # Update the plot with new data
        ax.clear()
        ax.plot(data_points, label='Data Stream')
        
        if anomaly_points:
            ax.scatter(*zip(*anomaly_points), color='red', label='Anomaly')
        
        ax.legend()
        plt.draw()
        plt.pause(0.01)  # Adjust for smooth updates

# Main Function to run the stream and detect anomalies
if __name__ == "__main__":
    stream = generate_data_stream()  # Starts the data stream
    detector = AnomalyDetector()     # Initializes the anomaly detector
    visualize_data(stream, detector) # Startss visualizing and detecting anomalies



class AnomalyDetector:
    def __init__(self, window_size=100, threshold=3):
        """
        Initializes the anomaly detector with a sliding window size and a Z-score threshold.
        The window size determines how many data points are used to calculate the moving average and standard deviation.
        The threshold determines what Z-Score is considered an anomaly.
        """
        self.window_size = window_size
        self.threshold = threshold
        self.data = deque(maxlen=window_size)
    
    def detect(self, new_value):
        """
        Detects anomalies based on Z-Score. Returns True if an anomaly is detected, else False.
        Z-Score measures how many standard deviations a value is from the mean.
        """
        if len(self.data) < self.window_size:
            # Not enough data points to calculate Z-Score yet
            self.data.append(new_value)
            return False
        
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        
        # Z-score calculation (handling zero standard deviation)
        z_score = (new_value - mean) / std_dev if std_dev > 0 else 0
        
        # Adds the new value to the sliding window
        self.data.append(new_value)
        
        # Checks if the Z-Score exceeds the anomaly threshold
        if abs(z_score) > self.threshold:
            return True
        else:
            return False


def visualize_data(stream, detector):
    """
    Plots the data stream in real-time and marks detected anomalies in red.
    """
    plt.ion()  # Turns on interactive mode
    fig, ax = plt.subplots()
    data_points = []
    anomaly_points = []
    
    for value in stream:
        data_points.append(value)
        is_anomaly = detector.detect(value)
        
        if is_anomaly:
            anomaly_points.append((len(data_points) - 1, value))
        
        # Update plot
        ax.clear()
        ax.plot(data_points, label='Data Stream')
        
        if anomaly_points:
            ax.scatter(*zip(*anomaly_points), color='red', label='Anomalies')
        
        ax.legend()
        plt.draw()
        plt.pause(0.01)  # Pause to allow real-time updates


if __name__ == "__main__":
    # Initializes data stream
    stream = generate_data_stream()
    
    # Initializes anomaly detector
    detector = AnomalyDetector(window_size=100, threshold=3)
    
    # Starts visualizing the data stream with anomaly detection
    visualize_data(stream, detector)


