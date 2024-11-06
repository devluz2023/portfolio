public class QuickSort {

    // Método principal que chama a função de ordenação
    public static void main(String[] args) {
        int[] array = { 10, 7, 8, 9, 1, 5 };
        System.out.println("Array original:");
        printArray(array);

        quickSort(array, 0, array.length - 1);

        System.out.println("Array ordenado:");
        printArray(array);
    }

    // Função de ordenação QuickSort
    static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            // Particiona o array e obtém o índice da partição
            int pi = partition(array, low, high);

            // Recursivamente ordena os elementos antes e depois da partição
            quickSort(array, low, pi - 1);
            quickSort(array, pi + 1, high);
        }
    }

    // Função para particionar o array
    static int partition(int[] array, int low, int high) {
        // O último elemento como pivô
        int pivot = array[high];
        int i = (low - 1); // Índice do menor elemento

        for (int j = low; j < high; j++) {
            // Se o elemento atual for menor ou igual ao pivô
            if (array[j] <= pivot) {
                i++;

                // Troca array[i] e array[j]
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        // Troca array[i + 1] e array[high] (ou pivô)
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;

        return i + 1; // Retorna o índice da partição
    }

    // Função para imprimir o array
    static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
