# Day 16 - Turtle & Object-Oriented Programming Basics

from turtle import Turtle, Screen

# Create objects from classes
tim = Turtle()
screen = Screen()

# Customize the turtle
tim.shape("turtle")
tim.color("DarkOliveGreen4")

# Move the turtle
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.left(45)
tim.back(50)

# Keep screen open on click
screen.exitonclick()