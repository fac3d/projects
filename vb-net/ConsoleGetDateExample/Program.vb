Imports System

Module ConsoleGetDateExample
    Sub Main()
        Console.WriteLine("Hello World!")
        Console.WriteLine(DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss"))
        Dim t = Date.Now
        Console.WriteLine("Time now is {0}", t)
        Dim testDate As DateTime = #3/12/1999#
        Console.WriteLine(testDate)
        Dim tDate As DateTime = Date.Now
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Day)
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Month)
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Year)
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Hour)
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Minute)
        Console.WriteLine(tDate)
        Console.WriteLine(tDate.Second)

        Dim d1 As Date = Now
        Dim d2 As Date = Now

        Dim days As Long = DateDiff(DateInterval.Day, d1, d2)
        Console.WriteLine(days)

        'Add 2 months
        Dim mValue As Integer = 2
        Dim dValue As DateTime = Date.Now
        Dim d3 As Date = DateAdd(DateInterval.Month, mValue, dValue)
        Console.WriteLine(d3)

        'Add 20 minutes, variables defined above
        Dim minValue As Integer = 20
        dValue = Date.Now
        d3 = DateAdd(DateInterval.Minute, minValue, dValue)
        Console.WriteLine(d3)

        'MMM is display month as Jan
        Dim tStr As String
        tStr = Format(d1, "dd-MMM-yyyy hh:mm:ss")
        Console.WriteLine(tStr)
        tStr = Format(d3, "dd-MMM-yyyy hh:mm:ss")
        Console.WriteLine(tStr)

    End Sub
End Module
