<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useRoomStore } from '@/stores/room'
import { useToast } from '@/composables/useToast'
import Button from '@/components/ui/Button.vue'
import Input from '@/components/ui/Input.vue'
import Avatar from '@/components/ui/Avatar.vue'
import AvatarImage from '@/components/ui/AvatarImage.vue'
import AvatarFallback from '@/components/ui/AvatarFallback.vue'
import ScrollArea from '@/components/ui/ScrollArea.vue'
import { Crown, Send, LogOut, Users, Copy, Loader2, Home, MessageSquare } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const roomStore = useRoomStore()
const { toast } = useToast()

const messageInput = ref('')
const messagesEndRef = ref(null)
const isInitialLoad = ref(true)

const scrollToBottom = () => {
  nextTick(() => {
    messagesEndRef.value?.scrollIntoView({ behavior: 'smooth' })
  })
}

watch(
  () => roomStore.messages,
  () => {
    scrollToBottom()
  },
  { deep: true }
)

onMounted(() => {
  isInitialLoad.value = false
  const hasSavedRoom = localStorage.getItem('activeRoom')
  if (!roomStore.activeRoom && !hasSavedRoom) {
    router.push('/dashboard')
  }
})

watch(
  () => [roomStore.activeRoom, roomStore.isReconnecting],
  ([activeRoom, isReconnecting]) => {
    if (isInitialLoad.value) return
    if (isReconnecting) return

    const hasSavedRoom = localStorage.getItem('activeRoom')
    if (!activeRoom && !hasSavedRoom) {
      router.push('/dashboard')
    }
  }
)

const isLeader = () => {
  return roomStore.activeRoom?.leaderId === authStore.user?.id
}

const handleSendMessage = () => {
  if (!messageInput.value.trim()) return
  roomStore.sendMessage(messageInput.value)
  messageInput.value = ''
}

const handleEndSession = async () => {
  await roomStore.endSession()
  toast({
    title: 'Sesi selesai',
    description: 'Room telah ditutup oleh leader.'
  })
  router.push('/dashboard')
}

const handleLeaveRoom = async () => {
  await roomStore.leaveRoom()
  toast({
    title: 'Keluar dari room',
    description: 'Anda telah meninggalkan tim.'
  })
  router.push('/dashboard')
}

const handleBackToDashboard = () => {
  roomStore.clearAutoNavigate()
  toast({
    title: 'Kembali ke Dashboard',
    description: 'Anda tetap terhubung di room ini.'
  })
  router.push('/dashboard')
}

const handleCopyRoomId = () => {
  navigator.clipboard.writeText(roomStore.activeRoom?.id || '')
  toast({
    title: 'Disalin',
    description: 'ID Room disalin ke clipboard.'
  })
}
</script>

<template>
  <div v-if="roomStore.isReconnecting" class="flex h-screen flex-col items-center justify-center bg-[#f4f8f5]">
    <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-slate-950">
      <Loader2 class="h-8 w-8 animate-spin text-emerald-300" />
    </div>
    <h2 class="mb-2 text-xl font-semibold text-slate-950">Menghubungkan...</h2>
    <p class="text-sm text-slate-500">Menghubungkan kembali ke room</p>
  </div>

  <div v-else-if="!roomStore.activeRoom && localStorage.getItem('activeRoom')" class="flex h-screen flex-col items-center justify-center bg-[#f4f8f5]">
    <div class="mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-slate-950">
      <Loader2 class="h-8 w-8 animate-spin text-emerald-300" />
    </div>
    <h2 class="mb-2 text-xl font-semibold text-slate-950">Memuat Room</h2>
    <p class="text-sm text-slate-500">Mohon tunggu sebentar...</p>
  </div>

  <div v-else-if="!roomStore.activeRoom"></div>

  <div v-else class="flex h-screen bg-[#f4f8f5] text-slate-800">
    <aside class="hidden w-[280px] flex-col border-r border-slate-200 bg-white lg:flex">
      <div class="border-b border-slate-100 p-4">
        <div class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-2xl bg-slate-950">
            <Users class="h-5 w-5 text-emerald-300" />
          </div>
          <div>
            <p class="font-semibold text-slate-950">GroupMatch</p>
            <p class="text-xs text-slate-500">Team room</p>
          </div>
        </div>
      </div>

      <div class="border-b border-slate-100 p-4">
        <p class="text-xs font-medium uppercase text-slate-400">Room ID</p>
        <div class="mt-2 flex items-center gap-2">
          <code class="min-w-0 flex-1 truncate rounded-xl bg-slate-50 px-3 py-2 font-mono text-sm text-slate-700">
            {{ roomStore.activeRoom?.id ? String(roomStore.activeRoom.id).slice(-8) : '...' }}
          </code>
          <Button size="icon" variant="outline" class="h-9 w-9 rounded-xl border-slate-200" @click="handleCopyRoomId">
            <Copy class="h-4 w-4" />
          </Button>
        </div>
      </div>

      <div class="flex min-h-0 flex-1 flex-col p-4">
        <div class="mb-3 flex items-center justify-between">
          <p class="text-sm font-semibold text-slate-950">Anggota</p>
          <span class="text-xs text-slate-500">{{ roomStore.activeRoom?.members?.length || 0 }} orang</span>
        </div>

        <div class="min-h-0 flex-1 space-y-1 overflow-y-auto">
          <div v-if="!roomStore.activeRoom?.members || roomStore.activeRoom.members.length === 0" class="py-4 text-center">
            <p class="text-sm text-slate-400">Memuat anggota...</p>
          </div>
          <div
            v-for="m in roomStore.activeRoom?.members || []"
            :key="m.id"
            :class="[
              'flex gap-3 rounded-2xl p-3 transition-colors',
              m.id === authStore.user?.id ? 'bg-emerald-50' : 'hover:bg-slate-50'
            ]"
          >
            <Avatar class="h-9 w-9">
              <AvatarImage :src="m.avatar || ''" />
              <AvatarFallback class="bg-emerald-600 text-xs text-white">
                {{ m.name?.[0] || 'U' }}
              </AvatarFallback>
            </Avatar>
            <div class="min-w-0 flex-1">
              <p class="flex items-center gap-1 truncate text-sm font-medium text-slate-800">
                <template v-if="m.id === authStore.user?.id">Kamu</template>
                <template v-else>{{ m.name || m.username || `User ${String(m.id).slice(-4)}` }}</template>
                <Crown v-if="m.id === roomStore.activeRoom?.leaderId" class="h-3.5 w-3.5 text-amber-500" />
              </p>
              <p class="truncate text-xs text-slate-500">
                {{ m.role || 'Member' }}<template v-if="m.username"> - @{{ m.username }}</template>
              </p>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <main class="flex min-w-0 flex-1 flex-col">
      <header class="border-b border-slate-200 bg-white/85 px-4 py-3 backdrop-blur-xl">
        <div class="flex flex-wrap items-center justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <MessageSquare class="h-5 w-5 text-emerald-600" />
              <h1 class="text-lg font-semibold text-slate-950">Diskusi Tim</h1>
            </div>
            <p class="mt-1 text-xs text-slate-500">Gunakan ruang ini untuk koordinasi dan pembagian tugas.</p>
          </div>
          <div class="flex flex-wrap justify-end gap-2">
            <Button variant="ghost" size="sm" class="rounded-xl" @click="handleBackToDashboard">
              <Home class="mr-2 h-4 w-4" /> Dashboard
            </Button>
            <Button v-if="isLeader()" variant="destructive" size="sm" class="rounded-xl" @click="handleEndSession">
              <Crown class="mr-2 h-4 w-4" /> End Session
            </Button>
            <Button variant="outline" size="sm" class="rounded-xl border-slate-200 bg-white" @click="handleLeaveRoom">
              <LogOut class="mr-2 h-4 w-4" /> Keluar
            </Button>
          </div>
        </div>
      </header>

      <section class="flex min-h-0 flex-1 flex-col p-4">
        <div class="flex min-h-0 flex-1 flex-col overflow-hidden rounded-[1.5rem] border border-slate-200 bg-white shadow-sm">
          <ScrollArea class="max-h-none flex-1 p-5">
            <div class="space-y-5">
              <div v-if="roomStore.messages.length === 0" class="py-16 text-center">
                <div class="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-emerald-50">
                  <Send class="h-7 w-7 text-emerald-300" />
                </div>
                <p class="text-sm font-medium text-slate-500">Belum ada pesan</p>
                <p class="mt-1 text-xs text-slate-400">Mulai percakapan dengan timmu.</p>
              </div>

              <div
                v-for="msg in roomStore.messages"
                :key="msg.id"
                :class="['flex gap-3', msg.userId === authStore.user?.id ? 'flex-row-reverse' : '']"
              >
                <Avatar class="h-9 w-9 flex-shrink-0">
                  <AvatarFallback :class="[
                    'text-xs',
                    msg.userId === authStore.user?.id ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700'
                  ]">
                    {{ msg.username?.[0] || 'U' }}
                  </AvatarFallback>
                </Avatar>
                <div :class="['max-w-[78%]', msg.userId === authStore.user?.id ? 'text-right' : '']">
                  <p class="mb-1 px-1 text-xs text-slate-400">
                    {{ msg.userId === authStore.user?.id ? 'Kamu' : msg.username }}
                  </p>
                  <div :class="[
                    'rounded-[1.25rem] px-4 py-3 text-sm leading-6',
                    msg.userId === authStore.user?.id
                      ? 'rounded-br-md bg-slate-950 text-white'
                      : 'rounded-bl-md bg-slate-100 text-slate-700'
                  ]">
                    {{ msg.text }}
                  </div>
                </div>
              </div>
              <div ref="messagesEndRef" />
            </div>
          </ScrollArea>

          <form @submit.prevent="handleSendMessage" class="border-t border-slate-100 bg-white p-3">
            <div class="flex gap-2 rounded-2xl bg-slate-50 p-2">
              <Input
                v-model="messageInput"
                placeholder="Tulis pesan..."
                class="h-11 flex-1 border-0 bg-transparent focus-visible:ring-0 focus-visible:ring-offset-0"
              />
              <Button
                type="submit"
                :disabled="!messageInput.trim()"
                class="h-11 rounded-xl bg-slate-950 px-5 text-emerald-100 hover:bg-slate-800"
              >
                <Send class="h-4 w-4" />
              </Button>
            </div>
          </form>
        </div>
      </section>
    </main>
  </div>
</template>
