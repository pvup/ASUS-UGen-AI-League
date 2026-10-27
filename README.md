# Smart Desk Inventory

AI-Powered Missing Item Detection System

## Overview

Smart Desk Inventory is a lightweight computer vision prototype developed for the 2026 ASUS UGen AI League Hackathon.

The system detects objects through a webcam and provides real-time alerts when an expected item is missing.

## Features

- Real-time object detection using YOLOv8n
- Webcam-based inventory monitoring
- Automatic missing item alerts
- Visual status indicators: WAITING, PRESENT, CHECKING, MISSING
- CPU inference without requiring a dedicated GPU

## Technology

- Python 3.11
- Ultralytics YOLOv8n
- OpenCV
- PyTorch

## Installation

Create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    python -m pip install -r requirements.txt

Run the application:

    python demo.py

Press q to exit.

## Current Prototype

The current implementation monitors the presence of a cup.

When the cup disappears for a predefined number of inference frames, the system displays a MISSING alert.

Detection performance may vary with lighting, camera angle, and object occlusion.

## Hardware

Current development and testing:
- Apple MacBook M1 Pro
- CPU-based inference

Proposed future deployment:
- ASUS UGen300 AI Accelerator
- Hailo-10H

The current prototype has not yet been deployed or benchmarked on ASUS UGen300.

## Hackathon

2026 ASUS UGen AI League

Category: Workplace AI

Track: Battlefield Lightning
