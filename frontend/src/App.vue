<script setup>
import { onMounted, computed } from 'vue'
import { RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { MOCK_MODE } from '@/services/api'
import Toaster from '@/components/ui/Toaster.vue'
import { Loader2, Users } from 'lucide-vue-next'

const authStore = useAuthStore()

onMounted(() => {
  authStore.initAuth()
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
