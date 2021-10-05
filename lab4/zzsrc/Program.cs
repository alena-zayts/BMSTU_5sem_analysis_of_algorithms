using System;
using System.Diagnostics;
using System.Threading;
class Program
{
	static void Main(string[] args)
	{
		Stopwatch stopWatch = new Stopwatch();
		stopWatch.Start();
		Thread.Sleep(2900);
		stopWatch.Stop();
		// Get the elapsed time as a TimeSpan value.
		TimeSpan ts = stopWatch.Elapsed;

		Console.WriteLine(ts.Seconds + "." + ts.Milliseconds);
		Console.WriteLine(ts);

		// Format and display the TimeSpan value.
		string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
			ts.Hours, ts.Minutes, ts.Seconds,
			ts.Milliseconds / 10);
		Console.WriteLine("RunTime " + elapsedTime);
	}
}

// using System;
// using System.Threading;
// class Program
// {
// 	static Mutex mutexObj = new Mutex();
// 	static int x = 0;

// 	static void Main(string[] args)
// 	{
// 		for (int i = 0; i < 5; i++)
// 		{
// 			Thread myThread = new Thread(Count);
// 			myThread.Name = $"Поток {i}";
// 			myThread.Start();
// 		}

// 		Console.ReadLine();
// 	}
// 	public static void Count()
// 	{
// 		mutexObj.WaitOne();
// 		x = 1;
// 		for (int i = 1; i < 9; i++)
// 		{
// 			Console.WriteLine($"{Thread.CurrentThread.Name}: {x}");
// 			x++;
// 			Thread.Sleep(100);
// 		}
// 		mutexObj.ReleaseMutex();
// 	}
// }
// class Program
// {
// 	static void Main(string[] args)
// 	{
// 		int number = 4;
// 		// создаем новый поток
// 		Thread myThread = new Thread(new ParameterizedThreadStart(Count));
// 		myThread.Start(number);

// 		for (int i = 1; i < 9; i++)
// 		{
// 			Console.WriteLine("Главный поток:");
// 			Console.WriteLine(i * i);
// 			Thread.Sleep(300);
// 		}

// 		Console.ReadLine();
// 	}

// 	public static void Count(object x)
// 	{
// 		for (int i = 1; i < 9; i++)
// 		{
// 			int n = (int)x;

// 			Console.WriteLine("Второй поток:");
// 			Console.WriteLine(i * n);
// 			Thread.Sleep(400);
// 		}
// 	}
// }



// class Program
// {
// 	static void Main(string[] args)
// 	{
// 		// создаем новый поток
// 		Thread myThread = new Thread(new ThreadStart(Count));
// 		myThread.Start(); // запускаем поток

// 		for (int i = 1; i < 19; i++)
// 		{
// 			Console.WriteLine("Главный поток:");
// 			Console.WriteLine(i * i);
// 			Thread.Sleep(300);
// 		}

// 	}

// 	public static void Count(int a, int b)
// 	{
// 		for (int i = 1; i < 19; i++)
// 		{
// 			Console.WriteLine("Второй поток:");
// 			Console.WriteLine(i * i);
// 			Thread.Sleep(400);
// 		}
// 	}
// }


// // using System;
// // using System.Threading;

// // namespace Lab_04
// // {
// // 	static class Program
// // 	{
// // 		public static void CallToChildThread()
// // 		{
// // 			// Console.WriteLine("Child thread starts");
// // 			for (int i = 0; i < 10; i++)
// // 				Console.WriteLine("Поток 1");
// // 		}
// // 		static void Main(string[] args)
// // 		{
// // 			Thread childThread = new Thread(new ThreadStart(CallToChildThread));
// // 			childThread.Start();
// // 			for (int i = 0; i < 10; i++)
// // 				Console.WriteLine("Главный поток");
// // 			// childThread2.Start();
// // 		}
// // 	}
// // }