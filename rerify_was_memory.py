from java.lang.management import ManagementFactory

class MemoryUsageInfo:
    def __init__(self):
        # Obter o MemoryMXBean para acessar informações de memória
        self.memory_bean = ManagementFactory.getMemoryMXBean()
        
        # Inicializar valores de heap e non-heap
        self.heap_memory_usage = self.memory_bean.getHeapMemoryUsage()
        self.non_heap_memory_usage = self.memory_bean.getNonHeapMemoryUsage()

    def get_memory_info(self, memory_usage):
        """Retorna um dicionário com informações sobre a memória em bytes."""
        used_bytes = memory_usage.getUsed()
        committed_bytes = memory_usage.getCommitted()
        max_bytes = memory_usage.getMax()
    
        return {
            "used": used_bytes,
            "committed": committed_bytes,
            "max": max_bytes
        }

    def get_heap_memory_info(self):
        """Retorna um dicionário com informações sobre a memória heap em bytes."""
        return self.get_memory_info(self.heap_memory_usage)

    def get_non_heap_memory_info(self):
        """Retorna um dicionário com informações sobre a memória non-heap em bytes."""
        return self.get_memory_info(self.non_heap_memory_usage)


    def display_memory_info(self):
        """Exibe as informações de memória heap, non-heap e o total formatadas em bytes."""
        heap_info = self.get_heap_memory_info()
        non_heap_info = self.get_non_heap_memory_info()
        
        total_committed = heap_info['committed'] + non_heap_info['committed']

        print("===== Informações de Memória =====")
        print("Memória Heap em uso: %d bytes" % heap_info['used'])
        print("Memória Heap total comprometida: %d bytes" % heap_info['committed'])
        print("Memória Heap máxima possível: %d bytes" % heap_info['max'])

        print("\nMemória Non-Heap em uso: %d bytes" % non_heap_info['used'])
        print("Memória Non-Heap total comprometida: %d bytes" % non_heap_info['committed'])
        print("Memória Non-Heap máxima possível: %d bytes" % non_heap_info['max'])

        print("\nTotal de memória alocada (Heap + Non-Heap): %d bytes" % total_committed)

# Instanciar a classe e exibir informações de memória
if __name__ == "__main__":
    memory_info = MemoryUsageInfo()
    memory_info.display_memory_info()
