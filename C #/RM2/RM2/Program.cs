
using System;

namespace AnalizaENotave
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Mirësevini në programin e Analizës së Notave!");

            const int numriMaxNotave = 10;
            int[] nota = new int[numriMaxNotave];


            Console.WriteLine("Vendosni notat e studentëve (deri në 10 nota):");
            for (int i = 0; i < numriMaxNotave; i++)
            {
                Console.Write($"Shkruani notën {i + 1}: ");
                nota[i] = Convert.ToInt32(Console.ReadLine());
            }


            Console.WriteLine("\nNotat e futura janë:");
            ShfaqNota(nota);


            int notaMaksimale = GjejNotenMaksimale(nota);
            int notaMinimale = GjejNotenMinimale(nota);
            double mesatarja = LlogaritMesataren(nota);

            Console.WriteLine($"\nNota më e lartë: {notaMaksimale}");
            Console.WriteLine($"Nota më e ulët: {notaMinimale}");
            Console.WriteLine($"Mesatarja e notave: {mesatarja:F2}");


            const int pragKalimi = 60;
            int notaMbiPragun = NumroNotaMbiPragun(nota, 0, pragKalimi);

            Console.WriteLine($"Numri i notave mbi pragun {pragKalimi}: {notaMbiPragun}");
            Console.WriteLine("Faleminderit që përdorët programin!");
        }


        static void ShfaqNota(int[] nota)
        {
            for (int i = 0; i < nota.Length; i++)
            {
                Console.WriteLine(nota[i]);
            }
        }


        static int GjejNotenMaksimale(int[] nota)
        {
            int max = nota[0];
            for (int i = 1; i < nota.Length; i++)
            {
                if (nota[i] > max)
                    max = nota[i];
            }
            return max;
        }


        static int GjejNotenMinimale(int[] nota)
        {
            int min = nota[0];
            for (int i = 1; i < nota.Length; i++)
            {
                if (nota[i] < min)
                    min = nota[i];
            }
            return min;
        }


        static double LlogaritMesataren(int[] nota)
        {
            int shuma = 0;
            for (int i = 0; i < nota.Length; i++)
            {
                shuma += nota[i];
            }
            return (double)shuma / nota.Length;
        }


        static int NumroNotaMbiPragun(int[] nota, int index, int prag)
        {
            if (index == nota.Length)
                return 0;

            int count = nota[index] > prag ? 1 : 0;
            return count + NumroNotaMbiPragun(nota, index + 1, prag);
        }
    }
}
