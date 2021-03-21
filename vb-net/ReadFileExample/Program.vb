Imports System.IO

Module ReadFileExample
    Sub Main(args As String())

        ' Get command line arguments
        Dim sCmdLine As String = Environment.CommandLine()
        Console.WriteLine("CommandLine: " & sCmdLine)
        Dim iPos = sCmdLine.IndexOf("""", 2)
        Dim sCmdLineArgs = sCmdLine.Substring(iPos + 1).Trim()
        Console.WriteLine("CommandLine.Arguments: " & sCmdLineArgs)

        Try
            ' Create an instance of StreamReader to read from a file. 
            ' The using statement also closes the StreamReader.
            Dim FileName As String = "C:\Users\frank\Desktop\hello.txt"
            Using sr As StreamReader = New StreamReader(FileName)
                Console.WriteLine(FileName)
                Dim line As String
                ' Read and display lines from the file until the end of file
                line = sr.ReadLine()
                While (line <> Nothing)
                    Console.WriteLine(line)
                    line = sr.ReadLine()
                End While
                Dim info As New FileInfo(FileName)
                Console.WriteLine(info.Name)
                Console.WriteLine(info.Length)
                Console.WriteLine(info.Exists)
                Console.WriteLine(info.FullName)
                Console.WriteLine(info.CreationTime)
                Console.WriteLine(info.LastAccessTime)
            End Using
        Catch e As Exception
            ' Let the user know what went wrong.
            Console.WriteLine("Input File Read Error:")
            Console.WriteLine(e.Message)
        End Try
        ' Press key to exit program.
        Console.ReadKey()
    End Sub
End Module
