#!/usr/bin/env python3
"""
Test script for DeepSeek AI integration
"""

import requests
import json

def test_deepseek_endpoint():
    """Test the DeepSeek API endpoint"""
    print("🧪 Testing DeepSeek AI Integration...")
    print("=" * 50)
    
    # Test data
    test_question = "What are my legal rights if I've been wrongfully terminated from my job?"
    
    try:
        # Test the endpoint
        response = requests.post(
            'http://localhost:5000/api/deepseek_legal',
            headers={'Content-Type': 'application/json'},
            json={'question': test_question},
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ DeepSeek AI Integration Working!")
                print(f"Source: {result.get('source', 'Unknown')}")
                print(f"Model: {result.get('model', 'Unknown')}")
                print("\n📝 Response Preview:")
                answer = result.get('answer', '')
                print(answer[:200] + "..." if len(answer) > 200 else answer)
            else:
                print("❌ DeepSeek API Error:")
                print(result.get('error', 'Unknown error'))
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the Flask server is running")
        print("   Start it with: python app.py")
    except Exception as e:
        print(f"❌ Test Error: {e}")

def test_status_endpoint():
    """Test the status endpoint"""
    print("\n🔍 Testing Status Endpoint...")
    print("-" * 30)
    
    try:
        response = requests.get('http://localhost:5000/api/status', timeout=10)
        
        if response.status_code == 200:
            status = response.json()
            print("✅ Status Endpoint Working!")
            print(f"Server Status: {status.get('status', 'Unknown')}")
            print(f"Datasets Loaded: {status.get('datasets_loaded', 0)}")
            print(f"DeepSeek Available: {status.get('deepseek_available', False)}")
            print(f"Available Datasets: {', '.join(status.get('datasets', []))}")
        else:
            print(f"❌ Status Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Server not running")
    except Exception as e:
        print(f"❌ Status Test Error: {e}")

if __name__ == "__main__":
    print("LawHub DeepSeek Integration Test")
    print("=" * 50)
    
    # Test status first
    test_status_endpoint()
    
    # Test DeepSeek endpoint
    test_deepseek_endpoint()
    
    print("\n" + "=" * 50)
    print("Test completed!") 