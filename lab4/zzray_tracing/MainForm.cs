using System;
using System.Timers;
using System.Drawing;
using System.Windows.Forms;
using System.Collections.Generic;

using System.Diagnostics;
using System.Threading;

namespace Newton
{
	public class Limit
	{
		public Int32 begin;
		public Int32 end;
		public Limit(Int32 begin, Int32 end)
		{
			this.begin = begin;
			this.end = end;
		}

	}
	public class MainForm : Form
	{
		private List<Shape> _scene;
		private Bitmap _img; // Содержит растровое изображение.
		private PictureBox _imgBox; // Будет сожержать само изображение.
		public MainForm(List<Shape> scene)
		{
			SettingsWindows();
			InitializeComponent();
			_scene = scene;
		}

		#region SETTINGS
		private void SettingsWindows()
		{
			this.Text = "Newton\'s cradle";
			this.Width = (int)SizeObjects.WidthWindows;
			this.Height = (int)SizeObjects.HeightWindows;
			// Стиль рамки: 
			// Sizable - изменяем размер (по умолчанию).
			// None - без рамки.
			// Fixed3D - Фиксированная трехмерная граница.
			this.FormBorderStyle = FormBorderStyle.Sizable;
			// Убираем возможность развернуть окно во весь экран и сложить.
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			// Устанавливаем начальное положение окна в центре.
			this.StartPosition = FormStartPosition.CenterScreen;
		}
		private void InitializeComponent()
		{
			// Button Off/On.
			Button buttonOffOn = new Button();
			buttonOffOn.Text = "off/on";
			buttonOffOn.Location = new Point(550, 800);
			this.AcceptButton = buttonOffOn;
			buttonOffOn.Click += new EventHandler(ButtonOffOnClick);
			this.Controls.Add(buttonOffOn);

			// Image.
			_imgBox = new PictureBox();
			_imgBox.Size = new Size((int)SizeObjects.WidthCanvas, (int)SizeObjects.HeightCanvas);
			this.Controls.Add(_imgBox);
			_img = new Bitmap((int)SizeObjects.WidthCanvas, (int)SizeObjects.HeightCanvas);
			// _imgBox.Image = _img;

		}
		#endregion

		private void ButtonOffOnClick(object sender, System.EventArgs e)
		{
			DrawScene(150);

			// // int[] arrCount = { 1200, 600, 300, 150, 75 };

			// Stopwatch stopWatch = new Stopwatch();
			// stopWatch.Start();
			// // for (int j = 0; j < 50; j++)
			// FuncTrace();
			
			// stopWatch.Stop();
			// TimeSpan ts = stopWatch.Elapsed;
			// Console.WriteLine(ts.Seconds + "." + ts.Milliseconds);


			// List<string> listTime = new List<string>();

			// Stopwatch stopWatch = new Stopwatch();
			// TimeSpan ts;

			// // int[] arrCount = { 1200, 600, 300, 150, 75 };
			// int[] arrCount = { 75, 150, 300, 600, 1200 };

			// foreach (var elem in arrCount)
			// {
			// 	stopWatch.Start();
			// 	for (int j = 0; j < 10; j++)
			// 		DrawScene(elem);
			// 	stopWatch.Stop();
			// 	ts = stopWatch.Elapsed;
			// 	listTime.Add(ts.Seconds + "." + ts.Milliseconds);
			// }

			// foreach (var elem in listTime)
			// 	Console.WriteLine(elem);
		}
		public void FuncHorizontally(object obj)
		{
			Limit limit = (Limit)obj;
			for (Int32 i = limit.begin; i < limit.end; i++)
				for (Int32 j = 0; j < (int)SizeObjects.HeightCanvas; j++)
					_img.SetPixel(i, j, TraceRay(new Point(i, j)));
		}

		public void FuncVertically(object obj)
		{
			Limit limit = (Limit)obj;
			for (Int32 i = 0; i < (int)SizeObjects.WidthCanvas; i++)
				for (Int32 j = limit.begin; j < limit.end; j++)
					_img.SetPixel(i, j, TraceRay(new Point(i, j)));
		}

		private void FuncTrace()
		{
			for (Int32 i = 0; i < (int)SizeObjects.WidthCanvas; i++)
				for (Int32 j = 0; j < (int)SizeObjects.HeightCanvas; j++)
					_img.SetPixel(i, j, TraceRay(new Point(i, j)));

			_imgBox.Image = _img;
		}

		private void DrawScene(int step)
		{
			List<Thread> listThread = new List<Thread>();

			for (int i = 0; i < (int)SizeObjects.WidthCanvas - 16; i += step)
			{
				listThread.Add(new Thread(new ParameterizedThreadStart(FuncHorizontally)));
				listThread[listThread.Count - 1].Start(new Limit(i, i + step));
			}


			// Join — Это метод синхронизации, который блокирует вызывающий поток (то есть поток, который вызывает метод).
			// Используйте этот метод, чтобы убедиться, что поток был завершен.
			// То есть мы не пойдем далее по коду, пока что не выполнятся потоки, вызванные ранее 
			// (то есть те потоки, которые мы джоиним.).
			foreach (var elem in listThread)
			{
				// if (elem.ThreadState != System.Threading.ThreadState.Unstarted)
				elem.Join();
			}

			_imgBox.Image = _img;
		}

		private Color TraceRay(Point point)
		{
			Shape ClosestObject = null;
			double MinZ = Double.NegativeInfinity;

			foreach (var elem in _scene)
			{
				if (IsVisible((elem as Sphere).Radius, elem.Center.X - point.X, elem.Center.Y - point.Y))
				{
					if (elem.Center.Z > MinZ)
					{
						MinZ = elem.Center.Z;
						ClosestObject = elem;
					}
				}
			}

			if (ClosestObject == null)
				return Color.Black;

			Colors result = ClosestObject.Clr;
			return Color.FromArgb(result.R, result.G, result.B);
		}
		private bool IsVisible(double R, double dx, double dy)
		{
			// Это неправильное пересечение (но для лабы и это пойдет)
			if (Math.Pow(dx, 2.0d) + Math.Pow(dy, 2.0d) <= R * R)
				return true;
			return false;
		}

	}
}