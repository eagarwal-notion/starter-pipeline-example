#!/usr/bin/env python3
"""
Test suite for the rocket project.
Generates JUnit XML output for CI/CD integration.
"""

import unittest
import time
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestRocket(unittest.TestCase):
    """Test cases for rocket functionality."""

    def test_rocket_build(self):
        """Test that the rocket can be built successfully."""
        print("🔧 Starting rocket build process...")
        logger.info("Initializing rocket build sequence")
        
        # Simulate rocket building process
        time.sleep(0.1)  # Simulate some work
        rocket_components = ["engine", "fuel_tank", "guidance_system", "payload"]
        
        print(f"📦 Found {len(rocket_components)} components: {', '.join(rocket_components)}")
        logger.info(f"Component inventory: {rocket_components}")
        
        # Verify all components are available
        for component in rocket_components:
            self.assertIsNotNone(component)
        
        self.assertTrue(len(rocket_components) == 4)
        print("✅ Rocket build completed successfully!")

    def test_rocket_fuel_system(self):
        """Test rocket fuel system integrity."""
        print("⛽ Checking fuel system...")
        logger.info("Running fuel system diagnostics")
        
        time.sleep(0.05)
        fuel_level = 100
        fuel_type = "RP-1"
        
        print(f"📊 Fuel level: {fuel_level}%")
        print(f"🧪 Fuel type: {fuel_type}")
        logger.info(f"Fuel diagnostics - Level: {fuel_level}%, Type: {fuel_type}")
        
        self.assertEqual(fuel_level, 100)
        self.assertEqual(fuel_type, "RP-1")
        print("✅ Fuel system check passed!")

    def test_rocket_guidance_system(self):
        """Test rocket guidance system functionality."""
        print("🧭 Initializing guidance system...")
        logger.info("Starting guidance system calibration")
        
        time.sleep(0.08)
        coordinates = {"x": 0, "y": 0, "z": 0}
        target = {"x": 100, "y": 200, "z": 300}
        
        print(f"📍 Current coordinates: {coordinates}")
        print(f"🎯 Target coordinates: {target}")
        logger.info(f"Guidance data - Current: {coordinates}, Target: {target}")
        
        # Test coordinate system
        self.assertIsInstance(coordinates, dict)
        self.assertIn("x", coordinates)
        self.assertIn("y", coordinates)
        self.assertIn("z", coordinates)
        
        # Test target validation
        self.assertGreater(target["z"], 0)
        print("✅ Guidance system operational!")

    def test_rocket_payload_capacity(self):
        """Test rocket payload capacity limits."""
        print("📦 Checking payload capacity...")
        logger.info("Analyzing payload constraints")
        
        time.sleep(0.03)
        max_payload = 1000  # kg
        current_payload = 1250  # kg - INTENTIONALLY OVER LIMIT TO CAUSE FAILURE
        
        print(f"⚖️  Max payload capacity: {max_payload} kg")
        print(f"📊 Current payload: {current_payload} kg")
        logger.warning(f"Payload analysis - Max: {max_payload}kg, Current: {current_payload}kg")
        
        if current_payload > max_payload:
            print("❌ PAYLOAD OVERLOAD DETECTED!", file=sys.stderr)
            logger.error(f"Payload exceeds capacity by {current_payload - max_payload}kg")
        
        self.assertLessEqual(current_payload, max_payload, f"Payload {current_payload}kg exceeds maximum capacity {max_payload}kg")
        self.assertGreater(max_payload, 0)

    def test_rocket_safety_checks(self):
        """Test rocket safety system checks."""
        print("🛡️  Running safety system diagnostics...")
        logger.info("Initiating comprehensive safety checks")
        
        time.sleep(0.06)
        safety_systems = {
            "emergency_shutdown": True,
            "fire_suppression": True,
            "abort_system": True,
            "telemetry": True
        }
        
        print("🔍 Checking safety systems:")
        for system, status in safety_systems.items():
            status_emoji = "✅" if status else "❌"
            print(f"  {status_emoji} {system}: {'OPERATIONAL' if status else 'OFFLINE'}")
            logger.info(f"Safety system {system}: {'PASS' if status else 'FAIL'}")
        
        # All safety systems must be operational
        for system, status in safety_systems.items():
            self.assertTrue(status, f"Safety system {system} is not operational")
        
        print("✅ All safety systems operational!")

    def test_rocket_launch_sequence(self):
        """Test rocket launch sequence validation."""
        print("🚀 Validating launch sequence...")
        logger.info("Executing launch sequence verification")
        
        time.sleep(0.12)
        launch_steps = [
            "pre_flight_check",
            "fuel_loading", 
            "countdown",
            "ignition",
            "liftoff"
        ]
        
        print("📋 Launch sequence steps:")
        for i, step in enumerate(launch_steps, 1):
            print(f"  {i}. {step.replace('_', ' ').title()}")
            logger.info(f"Launch step {i}: {step}")
        
        # Verify launch sequence
        self.assertEqual(len(launch_steps), 5)
        self.assertEqual(launch_steps[0], "pre_flight_check")
        self.assertEqual(launch_steps[-1], "liftoff")
        
        print("✅ Launch sequence validated!")
        logger.info("Launch sequence validation completed successfully")


if __name__ == "__main__":
    unittest.main()