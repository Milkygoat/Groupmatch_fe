<script setup>
import { onMounted, computed, ref } from 'vue'
import { RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { MOCK_MODE } from '@/services/api'
import Toaster from '@/components/ui/Toaster.vue'
import { Users, Server } from 'lucide-vue-next'

const authStore = useAuthStore()
const serverInfo = ref(null)

onMounted(() => {
  authStore.initAuth()
  
  // Fetch info backend dari Load Balancer
  fetch('https://api.groupmatch.web.id/who')
    .then(res => res.json())
    .then(data => {
      serverInfo.value = data.server
    })
    .catch(() => {
      serverInfo.value = 'Unknown'
    })
})

const isLoading = computed(() => authStore.loading)
</script>

<template>
  <!-- Loading Screen -->
  <div
    v-if="isLoading"
    class="flex min-h-screen flex-col items-center justify-center bg-[#f7faf8]"
  >
    <div class="mb-4 flex h-16 w-16 animate-pulse items-center justify-center rounded-2xl bg-emerald-600 shadow-sm shadow-emerald-200">
      <Users class="h-8 w-8 text-white" />
    </div>
    <h2 class="text-xl font-semibold text-slate-900">GroupMatch</h2>
    <p class="text-slate-400 text-sm mt-2">Memuat...</p>
  </div>

  <!-- Main App -->
  <template v-else>
    <RouterView />

    <!-- Info Server Load Balancer -->
    <div
      v-if="serverInfo"
      class="fixed bottom-4 right-4 z-50 flex items-center gap-2 rounded-xl bg-emerald-600 px-4 py-2.5 text-sm font-medium text-white shadow-lg"
    >
      <Server class="w-4 h-4" />
      <span>🖥️ {{ serverInfo }} via Nginx LB (GCP)</span>
    </div>

    <!-- Mock Mode Banner -->
    <div
      v-if="MOCK_MODE"
      class="fixed bottom-4 left-4 z-50 flex items-center gap-2 rounded-xl bg-amber-500 px-4 py-2.5 text-sm font-medium text-white shadow-lg backdrop-blur-sm"
    >
      <div class="w-2 h-2 bg-white rounded-full animate-pulse"></div>
      <span>Mock Mode - UI Preview</span>
    </div>
  </template>

  <!-- Toast Notifications -->
  <Toaster />
</template>
