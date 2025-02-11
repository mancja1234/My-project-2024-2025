
using System;

class Program
{
    static void Main(string[] args)
    {
        int rows = 5;
        int cols = 3;
        int[,] notaStudentëve = new int[rows, cols];


        Console.WriteLine("Mirësevini në Menaxhimin e Rezultateve të Studentëve!");
        Console.WriteLine("Fusni rezultatin për secilin student dhe secilën lëndë:");


        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write($"Studenti {i + 1}, Lënda {j + 1}: ");
                notaStudentëve[i, j] = int.Parse(Console.ReadLine());
            }
        }


        Console.WriteLine("Matrica Fillestare e Rezultateve:");
        DisplayMatrix(notaStudentëve);


        Console.WriteLine("\nShuma dhe mesatarja për secilin student:");
        for (int i = 0; i < rows; i++)
        {
            int shuma = 0;
            for (int j = 0; j < cols; j++)
            {
                shuma += notaStudentëve[i, j];
            }
            double mesatarja = (double)shuma / cols;
            Console.WriteLine($"Studenti {i + 1} - Shuma: {shuma}, Mesatarja: {mesatarja:F2}");
        }


        Console.Write("\nKërkoni një rezultat në matricë: ");
        int rezultatKerkesë = int.Parse(Console.ReadLine());
        SearchResult(notaStudentëve, rezultatKerkesë);
    }

    static void DisplayMatrix(int[,] matrix)
    {
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = 0; j < matrix.GetLength(1); j++)
            {
                Console.Write($"{matrix[i, j]} ");
            }
            Console.WriteLine();
        }
    }

    static void SearchResult(int[,] matrix, int search)
    {
        bool found = false;
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = 0; j < matrix.GetLength(1); j++)
            {
                if (matrix[i, j] == search)
                {
                    Console.WriteLine($"Rezultati gjendet në Studentin {i + 1}, Lënda {j + 1}.");
                    found = true;
                }
            }
        }
        if (found)
        {
            Console.WriteLine($"Rezultati {search} nuk është i pranishëm në matricë.");
        }
    }
}
