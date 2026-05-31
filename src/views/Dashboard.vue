<script setup>
import { watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useRoomStore } from '@/stores/room'
import { useToast } from '@/composables/useToast'
import Button from '@/components/ui/Button.vue'
import Card from '@/components/ui/Card.vue'
import CardHeader from '@/components/ui/CardHeader.vue'
import CardTitle from '@/components/ui/CardTitle.vue'
import CardDescription from '@/components/ui/CardDescription.vue'
import CardContent from '@/components/ui/CardContent.vue'
import Badge from '@/components/ui/Badge.vue'
import Avatar from '@/components/ui/Avatar.vue'
import AvatarImage from '@/components/ui/AvatarImage.vue'
import AvatarFallback from '@/components/ui/AvatarFallback.vue'
import DropdownMenu from '@/components/ui/DropdownMenu.vue'
import DropdownMenuContent from '@/components/ui/DropdownMenuContent.vue'
import DropdownMenuItem from '@/components/ui/DropdownMenuItem.vue'
import DropdownMenuLabel from '@/components/ui/DropdownMenuLabel.vue'
import DropdownMenuSeparator from '@/components/ui/DropdownMenuSeparator.vue'
import {
  Tag,
  Users,
  LogOut,
  Loader2,
  Zap,
  Settings,
  UserCircle,
  ArrowRight,
  CheckCircle,
  Sparkles,
  MessageSquare,
} from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const roomStore = useRoomStore()
const { toast } = useToast()

onMounted(() => {
  roomStore.initRoom()
})

watch(
  () => [roomStore.activeRoom, roomStore.matchmakingStatus, roomStore.isNewMatch],
  ([activeRoom, matchmakingStatus, isNewMatch]) => {
    if (activeRoom && matchmakingStatus === 'matched' && isNewMatch) {
      setTimeout(() => router.push('/room'), 1200)
    }
  }
)

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}

const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="min-h-screen bg-[#f4f8f5] text-slate-800">
    <header class="sticky top-0 z-30 border-b border-slate-200/70 bg-white/85 backdrop-blur-xl">
      <div class="mx-auto flex max-w-6xl items-center justify-between px-4 py-3 sm:px-6">
        <router-link to="/dashboard" class="flex items-center gap-3">
          <div class="flex h-10 w-10 items-center justify-center rounded-2xl bg-slate-950">
            <Users class="h-5 w-5 text-emerald-300" />
          </div>
          <div>
            <p class="text-lg font-semibold text-slate-950">GroupMatch</p>
            <p class="hidden text-xs text-slate-500 sm:block">student workspace</p>
          </div>
        </router-link>

        <DropdownMenu v-slot="{ isOpen, toggle, close }">
          <Button variant="ghost" class="h-auto rounded-full px-2 py-1.5" @click="toggle">
            <Avatar class="ring-2 ring-emerald-100">
              <AvatarImage :src="authStore.user?.avatar" />
              <AvatarFallback class="bg-emerald-600 text-white">{{ authStore.user?.name?.[0] }}</AvatarFallback>
            </Avatar>
            <div class="ml-3 hidden text-left sm:block">
              <p class="text-sm font-semibold text-slate-900">{{ authStore.user?.name }}</p>
              <p class="text-xs text-slate-500">@{{ authStore.user?.username }}</p>
            </div>
          </Button>

          <DropdownMenuContent v-if="isOpen" align="end" class="w-56">
            <DropdownMenuLabel class="font-normal">
              <div class="flex flex-col space-y-1">
                <p class="text-sm font-medium">{{ authStore.user?.name }}</p>
                <p class="text-xs text-slate-500">{{ authStore.user?.email }}</p>
              </div>
            </DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem @click="navigateTo('/profile-setup'); close()" class="cursor-pointer">
              <UserCircle class="mr-2 h-4 w-4" /> Edit Profil
            </DropdownMenuItem>
            <DropdownMenuItem @click="toast({ title: 'Coming soon' }); close()" class="cursor-pointer">
              <Settings class="mr-2 h-4 w-4" /> Pengaturan
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem @click="handleLogout(); close()" class="cursor-pointer text-red-600 focus:text-red-600">
              <LogOut class="mr-2 h-4 w-4" /> Keluar
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </header>

    <main class="mx-auto max-w-6xl px-4 py-6 sm:px-6 lg:py-8">
      <section class="mb-6 flex flex-col justify-between gap-4 lg:flex-row lg:items-end">
        <div>
          <p class="text-sm font-medium text-emerald-700">Dashboard</p>
          <h1 class="mt-2 text-3xl font-semibold tracking-normal text-slate-950 sm:text-4xl">
            Hai, {{ authStore.user?.name }}.
          </h1>
          <p class="mt-3 max-w-2xl text-sm leading-6 text-slate-600">
            Kelola profil dan mulai matching tim sekarang.
          </p>
        </div>
        <Button variant="outline" class="w-fit rounded-2xl border-emerald-200 bg-white" @click="navigateTo('/profile-setup')">
          Edit Profil
        </Button>
      </section>

      <section class="grid gap-5 lg:grid-cols-[1.2fr_0.8fr]">
        <Card class="overflow-hidden rounded-[1.75rem] border-slate-200 bg-white shadow-sm">
          <CardContent class="p-0">
            <div class="bg-white p-6 text-slate-900 sm:p-8">
              <div class="flex items-start gap-4">
                <div class="flex h-14 w-14 flex-shrink-0 items-center justify-center rounded-2xl bg-emerald-50">
                  <Sparkles class="h-7 w-7 text-emerald-600" />
                </div>
                <div>
                  <p class="text-sm font-medium text-emerald-700">
                    {{ roomStore.activeRoom ? 'Room aktif' : 'Siap matching' }}
                  </p>
                  <h2 class="mt-2 text-2xl font-semibold leading-tight text-slate-950">
                    {{ roomStore.activeRoom ? 'Lanjutkan koordinasi timmu.' : 'Cari tim yang cocok dengan skill kamu.' }}
                  </h2>
                  <p class="mt-3 max-w-xl text-sm leading-6 text-slate-600">
                    {{ roomStore.activeRoom
                      ? 'Room masih tersedia untuk diskusi dan pembagian tugas.'
                      : 'Mulai pencarian untuk menemukan anggota yang saling melengkapi.' }}
                  </p>
                </div>
              </div>

              <div class="mt-7">
                <template v-if="roomStore.activeRoom">
                  <Button size="lg" class="h-12 rounded-2xl bg-emerald-600 px-7 text-white hover:bg-emerald-700" @click="navigateTo('/room')">
                    Kembali ke Room <ArrowRight class="ml-2 h-5 w-5" />
                  </Button>
                </template>
                <template v-else-if="roomStore.matchmakingStatus === 'searching'">
                  <div class="flex flex-col gap-4 sm:flex-row sm:items-center">
                    <div class="flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-50">
                      <Loader2 class="h-6 w-6 animate-spin text-emerald-600" />
                    </div>
                    <div>
                      <p class="font-medium text-slate-900">Mencari tim untukmu...</p>
                      <Button variant="outline" class="mt-3 rounded-xl border-slate-200 bg-white text-slate-700 hover:bg-slate-50 hover:text-slate-900" @click="roomStore.leaveRoom">
                        Batalkan
                      </Button>
                    </div>
                  </div>
                </template>
                <template v-else-if="roomStore.matchmakingStatus === 'matched'">
                  <div class="flex items-center gap-3">
                    <CheckCircle class="h-6 w-6 text-emerald-600" />
                    <p class="font-medium text-emerald-700">Tim ditemukan!</p>
                  </div>
                </template>
                <template v-else>
                  <Button size="lg" class="h-12 rounded-2xl bg-emerald-600 px-7 text-white hover:bg-emerald-700" @click="roomStore.startMatchmaking">
                    <Zap class="mr-2 h-5 w-5" /> Cari Tim Sekarang
                  </Button>
                </template>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card class="rounded-[1.75rem] border-slate-200 bg-white shadow-sm">
          <CardContent class="p-5">
            <div class="flex items-center gap-4">
              <Avatar class="h-16 w-16 ring-4 ring-emerald-50">
                <AvatarImage :src="authStore.user?.avatar" />
                <AvatarFallback class="bg-emerald-600 text-xl text-white">{{ authStore.user?.name?.[0] }}</AvatarFallback>
              </Avatar>
              <div class="min-w-0">
                <p class="truncate font-semibold text-slate-950">{{ authStore.user?.name }}</p>
                <p class="text-xs text-slate-500">@{{ authStore.user?.username }}</p>
                <Badge class="mt-2 bg-emerald-50 text-emerald-700">{{ authStore.user?.role || 'Member' }}</Badge>
              </div>
            </div>

            <div class="mt-5 border-t border-slate-100 pt-5">
              <div class="mb-3 flex items-center gap-2 text-sm font-semibold text-slate-900">
                <Tag class="h-4 w-4 text-emerald-600" />
                Skill
              </div>
              <div class="flex flex-wrap gap-2">
                <template v-if="authStore.user?.skills?.length">
                  <Badge v-for="(skill, index) in authStore.user.skills" :key="index" variant="outline">
                    {{ skill }}
                  </Badge>
                </template>
                <p v-else class="text-sm leading-6 text-slate-500">Belum ada skill ditambahkan.</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </section>

      <section class="mt-5">
        <Card class="rounded-[1.75rem] border-slate-200 bg-white shadow-sm">
          <CardHeader>
            <CardTitle class="flex items-center gap-2 text-lg font-semibold text-slate-950">
              <MessageSquare class="h-4 w-4 text-emerald-600" />
              Riwayat Tim
            </CardTitle>
            <CardDescription class="text-sm text-slate-500">Daftar aktivitas tim yang pernah kamu ikuti.</CardDescription>
          </CardHeader>
          <CardContent>
            <template v-if="roomStore.roomHistory.length === 0">
              <div class="rounded-[1.5rem] border border-dashed border-slate-200 bg-slate-50 p-8 text-center">
                <Users class="mx-auto h-8 w-8 text-slate-300" />
                <p class="mt-3 text-sm font-medium text-slate-500">Belum ada riwayat tim</p>
                <p class="mt-1 text-xs text-slate-400">Riwayat muncul setelah kamu bergabung dengan tim.</p>
              </div>
            </template>
            <template v-else>
              <div class="divide-y divide-slate-100">
                <div
                  v-for="(r, index) in roomStore.roomHistory"
                  :key="r.id"
                  class="flex items-center justify-between gap-4 py-4 first:pt-0 last:pb-0"
                >
                  <div>
                    <p class="font-medium text-slate-800">Room #{{ r.room_id ? String(r.room_id).slice(-6) : index + 1 }}</p>
                    <p class="mt-1 text-xs text-slate-500">{{ r.action }}</p>
                  </div>
                  <Badge variant="outline">Selesai</Badge>
                </div>
              </div>
            </template>
          </CardContent>
        </Card>
      </section>
    </main>
  </div>
</template>
