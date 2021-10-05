using System;
using System.Windows;

namespace Newton
{
	public class Colors
	{
		private byte _r, _g, _b;
		public Colors() { _r = _g = _b = 0; }
		public Colors(byte R, byte G, byte B) { _r = R; _g = G; _b = B; }
		public Colors(string str)
		{
			string[] param = str.Split(' ');
			if (param.Length == 3)
			{
				_r = Convert.ToByte(param[0]);
				_g = Convert.ToByte(param[1]);
				_b = Convert.ToByte(param[2]);
			}
			else
				_r = _g = _b = Byte.MinValue;
		}

		public byte R { get => _r; set => _r = value; }
		public byte G { get => _g; set => _g = value; }
		public byte B { get => _b; set => _b = value; }

		#region CHECK_BORDER
		private static byte _CheckLimits(double num)
		{
			if (num > byte.MaxValue)
				num = byte.MaxValue;
			else if (num < byte.MinValue)
				num = byte.MinValue;
			return (byte)num;
		}
		private static byte _CheckMax(double num)
		{
			if (num > byte.MaxValue)
				return byte.MaxValue;
			return (byte)num;
		}

		private static byte _CheckMin(double num)
		{
			if (num < byte.MinValue)
				return byte.MinValue;
			return (byte)num;
		}
		#endregion

		#region OPERATORS
		public static Colors operator +(Colors FirstColor, Colors SecondColor)
		{
			return new Colors(_CheckMax(FirstColor.R + SecondColor.R), _CheckMax(FirstColor.G + SecondColor.G), _CheckMax(FirstColor.B + SecondColor.B));
		}
		public static Colors operator +(Colors clr, double Intensity)
		{
			return new Colors(_CheckMax(clr.R + Intensity), _CheckMax(clr.G + Intensity), _CheckMax(clr.B + Intensity));
		}
		public static Colors operator *(Colors FirstColor, Colors SecondColor)
		{
			return new Colors(_CheckMax(FirstColor.R * SecondColor.R), _CheckMax(FirstColor.G * SecondColor.G), _CheckMax(FirstColor.B * SecondColor.B));
		}
		public static Colors operator *(Colors clr, double Intensity)
		{
			return new Colors(_CheckMax(clr.R * Intensity), _CheckMax(clr.G * Intensity), _CheckMax(clr.B * Intensity));
		}
		public static Colors operator -(Colors FirstColor, Colors SecondColor)
		{
			return new Colors(_CheckMin(FirstColor.R - SecondColor.R), _CheckMin(FirstColor.G - SecondColor.G), _CheckMin(FirstColor.B - SecondColor.B));
		}
		public static Colors operator -(Colors clr, double Intensity)
		{
			return new Colors(_CheckMin(clr.R - Intensity), _CheckMin(clr.G - Intensity), _CheckMin(clr.B - Intensity));
		}
		#endregion

		public override string ToString() => _r + " " + _g + " " + _b;
	}
}