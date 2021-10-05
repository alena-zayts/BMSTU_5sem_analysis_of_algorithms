FILES := *.cs

Program.exe: $(FILES)
	mcs $^ -pkg:dotnet -out:Program.exe

run:
	mono Program.exe data/scene.txt

clean:
	rm *.exe