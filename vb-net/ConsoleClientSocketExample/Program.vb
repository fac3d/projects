'
' Filename: Program.vb
'
' Project: ConsoleClientSocketExample
'
Imports System.Text
Imports System.Net.Sockets

Module ConsoleClientSocketExample
    Sub Main(args As String())
        Console.WriteLine("Press space bar to continue")
        Console.ReadKey()
        Dim IP As String = "192.168.1.107"
        Dim port As Int16 = 5001

        Dim tcpClient As New System.Net.Sockets.TcpClient()
        While (True)
            Try
                Console.WriteLine("About to connect")
                tcpClient.Connect(IP, port)
                Console.WriteLine("Connected")
                Dim networkStream As NetworkStream = tcpClient.GetStream()
                Dim sendBytes As Byte() = Encoding.ASCII.GetBytes("Hello There")
                networkStream.Write(sendBytes, 0, sendBytes.Length)
                Console.WriteLine("About to read from socket")
                Dim bytes(tcpClient.ReceiveBufferSize) As Byte
                networkStream.Read(bytes, 0, CInt(tcpClient.ReceiveBufferSize))
                Console.WriteLine("Length of tcpClientBufferSize is: {0}", tcpClient.ReceiveBufferSize)
                Dim returnData As String = System.Text.Encoding.ASCII.GetString(bytes)
                Console.WriteLine("Return data is: {0}, Length Is: {1}", returnData.Substring(0, 40), returnData.Length)
            Catch ex As SocketException
                Console.WriteLine("Socket Exception: {0}", ex.Message)
            Catch ex As System.IO.IOException
                Console.WriteLine("System IO Exception: {0}", ex.Message)
            Finally
                Console.WriteLine("Press space bar to continue")
                Console.ReadKey()
            End Try
        End While
        Console.WriteLine()
    End Sub
End Module
