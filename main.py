# Fyreworld is a open source product used to run custom tests on ec2
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='fyreworld arguments')
    parser.add_argument('--run-instances', help='Argument to run instances')
