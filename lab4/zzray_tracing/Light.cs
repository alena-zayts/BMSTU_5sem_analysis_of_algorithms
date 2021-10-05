using System;
using System.Drawing;
using System.Windows;

namespace Newton
{
	public class Light
	{
		private Vector _position;
		private double _intensity;
		public Vector Position { get => _position; }
		public double Intensity { get => _intensity; }
		public Light(Vector position, double intensity) { _position = position; _intensity = intensity; }

		public override string ToString() => "Position = " + _position + " Intensity = " + _intensity + "\n\n";
	}
}