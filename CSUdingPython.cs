using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            StringBuilder code = new StringBuilder();
            String input;
            while ((input = Console.ReadLine()) != "!q") //直到退出
            {
                code.AppendLine(input);
            }

            var file = File.CreateText("tmp.py");
            file.Write(code.ToString());
            file.Close(); //输出到临时文件，方便python执行

            System.Diagnostics.Process p = new System.Diagnostics.Process();
            p.StartInfo.FileName = "python"; //这样来调用python，需要将python加入Path环境变量内
            p.StartInfo.Arguments = "tmp.py";
            p.StartInfo.UseShellExecute = false;    //是否使用操作系统shell启动
            p.StartInfo.RedirectStandardInput = true;//接受来自调用程序的输入信息
            p.StartInfo.RedirectStandardOutput = true;//由调用程序获取输出信息
            p.StartInfo.RedirectStandardError = true;//重定向标准错误输出
            p.StartInfo.CreateNoWindow = true;//不显示程序窗口
            p.Start();//启动程序

            p.StandardInput.AutoFlush = true;



            //获取输出信息
            string output = p.StandardOutput.ReadToEnd();

            p.WaitForExit();//等待程序执行完退出进程
            p.Close();

            Console.WriteLine(output);
            Console.ReadKey(true);
        }
    }
}
