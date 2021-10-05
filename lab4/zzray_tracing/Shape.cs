using System;
using System.Drawing;
using System.Windows;

namespace Newton
{
	public class Shape
	{
		protected Vector _center;
		protected Colors _clr;
		public Vector Center { get => _center; set => _center = value; }
		public Colors Clr { get => _clr; }
		public Shape() { _clr = new Colors(); }
		public Shape(Vector Center, Colors clr) { _center = Center; _clr = clr; }

		public override string ToString() => "Center = " + _center + " " + "\nColor = " + _clr + "\n";
	}
	public class Sphere : Shape
	{
		private double _radius;
		public double Radius { get => _radius; }
		public Sphere(Vector Center, double Radius, Colors clr) : base(Center, clr) => _radius = Radius;

		public override string ToString() => base.ToString() + "Radius = " + _radius + "\n\n";
	}
}


