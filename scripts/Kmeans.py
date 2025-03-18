from manim import *
import numpy as np

class KMeansClustering(Scene):
    def construct(self):
        config.frame_width = 30
        config.frame_height = 18

        grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-10, 10, 1))
        self.add(grid)
        self.wait(0.5)

        np.random.seed(22)
        data = np.random.randn(15, 2) * 1
        data[:10, :] += np.array([3, 3])  				# First cluster 
        data[10:, :] += np.array([-3, -2])  			# Second cluster
        data_3d = np.hstack([data, np.zeros((15, 1))])  # To 3D for displaying

        
        centroids = data_3d[[0, 12]]  					# Picking 2 points to be the centroid
        data_3d = np.delete(data_3d, [0, 12], axis=0)  	# Deleteing the centroid of the points list (only for visualization purposes)
        points = [Dot(point, color=WHITE) for point in data_3d]

        centroid_dots = [
            Dot(centroids[0], color=RED, radius=0.15),  # Centroid for the first cluster (RED)
            Dot(centroids[1], color=BLUE, radius=0.15)  # Centroid for the second cluster (BLUE)
        ]
        centroid_labels = [
            Text(f"Centroid {i+1}", color=centroid_dots[i].get_color(), font_size = 20).next_to(centroid_dots[i], UP)
            for i in range(2)
        ]

        # VGroup creation for each centroid to be able to move them at the same time
        centroid_group_1 = VGroup(centroid_dots[0], centroid_labels[0])  
        centroid_group_2 = VGroup(centroid_dots[1], centroid_labels[1])  

		# Displaying first frame
        self.play(*[Create(point) for point in points])
        self.play(Create(centroid_group_1), Create(centroid_group_2))
        self.wait()

        # Step 1 : Choose a point to compute his distance to both centroids
        target_point = points[2]
        self.play(target_point.animate.set_color(YELLOW))  # Highlighting the point
        self.wait()

        # Creating lines
        distance_lines = []
        distance_texts = []
        for centroid in centroid_dots:
            line = Line(target_point.get_center(), centroid.get_center(), color=WHITE)
            distance = np.linalg.norm(target_point.get_center() - centroid.get_center())
            text = Text(f"{distance:.2f}", font_size=20).next_to(line, LEFT,  buff=0.1)
            distance_lines.append(line)
            distance_texts.append(text)

        # Displaying Distances and lines only for the first points
        self.play(*[Create(line) for line in distance_lines])
        self.play(*[Write(text) for text in distance_texts])
        self.wait(2)

        # Set the corresponding cluster to the point
        cluster = np.argmin([line.get_length() for line in distance_lines]).item()  
        new_color = centroid_dots[cluster].get_color()  # Set the corresponding color
        self.play(
            target_point.animate.set_color(new_color),
            *[FadeOut(line) for line in distance_lines],
            *[FadeOut(text) for text in distance_texts]
        )
        self.wait()

        # Step 2 : Same as step 1 but more faster for the other points
        clusters = []  
        for point in points:
            distances = [
                np.linalg.norm(point.get_center() - centroid.get_center())
                for centroid in centroid_dots
            ]
            cluster = np.argmin(distances).item() 
            clusters.append(cluster)

        colors = [centroid_dots[cluster].get_color() for cluster in clusters]
        self.play(*[point.animate.set_color(color) for point, color in zip(points, colors)], run_time=2)
        self.wait()

        # Step 3 : Computation of new centroids 
        new_centroids = []
        for i in range(2):  # For each cluster
            cluster_points = [point.get_center() for point, cluster in zip(points, clusters) if cluster == i]
            if len(cluster_points) > 0:
                new_centroid = np.mean(cluster_points, axis=0)
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroid_dots[i].get_center())  # Same centroid if no points

        # Formula display
        eq_text = MathTex(r"\text{New centroid} = \frac{1}{n}\sum_{i=1}^n x_i", color=WHITE).move_to([-1,3,0])
        
        # Move both centroid
        self.play(
            Write(eq_text),
			centroid_group_1.animate.move_to(new_centroids[0]),
            centroid_group_2.animate.move_to(new_centroids[1]),
            run_time=2
        )
        self.wait()
	
        self.play(FadeOut(eq_text))
        self.wait(2)
