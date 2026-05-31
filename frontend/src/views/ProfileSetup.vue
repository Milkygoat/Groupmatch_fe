<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from '@/composables/useToast'
import { ROLES } from '@/mock/mockData'
import Button from '@/components/ui/Button.vue'
import Input from '@/components/ui/Input.vue'
import Label from '@/components/ui/Label.vue'
import Card from '@/components/ui/Card.vue'
import CardHeader from '@/components/ui/CardHeader.vue'
import CardTitle from '@/components/ui/CardTitle.vue'
import CardDescription from '@/components/ui/CardDescription.vue'
import CardContent from '@/components/ui/CardContent.vue'
import Badge from '@/components/ui/Badge.vue'
import Avatar from '@/components/ui/Avatar.vue'
import AvatarImage from '@/components/ui/AvatarImage.vue'
import AvatarFallback from '@/components/ui/AvatarFallback.vue'
import Select from '@/components/ui/Select.vue'
import SelectItem from '@/components/ui/SelectItem.vue'
import { User, Calendar, Briefcase, Tag, X, Camera } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const { toast } = useToast()

const fileInputRef = ref(null)
const isSubmitting = ref(false)
const loading = ref(false)

const formData = ref({
  name: '',
  birthdate: '',
  role: '',
  skills: [],
  avatar: ''
})

const avatarFile = ref(null)
const skillInput = ref('')

onMounted(() => {
  if (authStore.user) {
    formData.value = {
      name: authStore.user.name || '',
      birthdate: authStore.user.birthdate || '',
      role: authStore.user.role || '',
      skills: authStore.user.skills || [],
      avatar: authStore.user.avatar || ''
    }
  }
})

const handleImageUpload = (e) => {
  const file = e.target.files[0]
  if (file) {
    if (file.size > 2 * 1024 * 1024) {
      toast({
        title: 'File terlalu besar',
        description: 'Maksimal ukuran file adalah 2MB',
        variant: 'destructive'
      })
      return
    }

    avatarFile.value = file

    const reader = new FileReader()
    reader.onloadend = () => {
      formData.value.avatar = reader.result
    }
    reader.readAsDataURL(file)
  }
}

const handleAddSkill = () => {
  if (skillInput.value.trim() && !formData.value.skills.includes(skillInput.value.trim())) {
    formData.value.skills.push(skillInput.value.trim())
    skillInput.value = ''
  }
}

const handleRemoveSkill = (skillToRemove) => {
  formData.value.skills = formData.value.skills.filter(skill => skill !== skillToRemove)
}

const handleSubmit = async () => {
  if (isSubmitting.value) return

  if (!formData.value.name || !formData.value.birthdate || !formData.value.role || formData.value.skills.length === 0) {
    toast({
      title: 'Data tidak lengkap',
      description: 'Silakan lengkapi semua field.',
      variant: 'destructive'
    })
    return
  }

  isSubmitting.value = true
  loading.value = true

  try {
    await authStore.updateProfile({
      name: formData.value.name,
      birthdate: formData.value.birthdate,
      role: formData.value.role,
      skills: formData.value.skills
    })

    if (avatarFile.value) {
      const uploadResponse = await authStore.uploadAvatar(avatarFile.value)
      console.log('Avatar uploaded:', uploadResponse.avatar_url)
    }

    toast({
      title: 'Profil berhasil disimpan!',
      description: 'Anda dapat mulai mencari tim.'
    })

    // Clear pending registration flag (if any) then go to dashboard
    try { localStorage.removeItem('pendingProfileSetupEmail') } catch (e) { /* ignore */ }
    router.push('/dashboard')
  } catch (error) {
    console.error('Profile update failed:', error)

    toast({
      title: 'Gagal Menyimpan',
      description: error.response?.data?.detail || 'Terjadi kesalahan saat menyimpan profil.',
      variant: 'destructive'
    })

    isSubmitting.value = false
    loading.value = false
  }
}

const selectRole = (value) => {
  formData.value.role = value
}
</script>

<template>
  <div class="min-h-screen bg-[#f5faf7] px-4 py-8 text-slate-800">
    <div class="mx-auto max-w-3xl">
      <Card class="rounded-[2rem] border-emerald-100 bg-white shadow-xl shadow-emerald-100/50">
        <CardHeader class="border-b border-emerald-100 px-6 py-6">
          <CardTitle class="text-2xl font-semibold text-slate-950">Lengkapi profil belajar</CardTitle>
          <CardDescription class="text-sm leading-6 text-slate-500">
            Isi data utama yang dibutuhkan untuk proses pencarian tim.
          </CardDescription>
        </CardHeader>

        <CardContent class="p-6">
          <form @submit.prevent="handleSubmit" class="space-y-7">
            <div class="flex flex-col items-center rounded-3xl border border-emerald-100 bg-emerald-50/60 p-5 sm:flex-row sm:items-center sm:justify-between">
              <div class="flex items-center gap-4">
                <div class="group relative cursor-pointer" @click="fileInputRef?.click()">
                  <Avatar class="h-24 w-24 border-4 border-white shadow-md">
                    <AvatarImage :src="formData.avatar" alt="Profile" class="object-cover" />
                    <AvatarFallback class="bg-white text-2xl text-emerald-700">
                      {{ formData.name ? formData.name.charAt(0).toUpperCase() : 'U' }}
                    </AvatarFallback>
                  </Avatar>
                  <div class="absolute inset-0 flex items-center justify-center rounded-full bg-black/40 opacity-0 transition-opacity group-hover:opacity-100">
                    <Camera class="h-8 w-8 text-white" />
                  </div>
                  <div class="absolute bottom-0 right-0 rounded-full border-2 border-white bg-emerald-600 p-2 shadow-sm">
                    <Camera class="h-4 w-4 text-white" />
                  </div>
                </div>
                <div>
                  <p class="font-semibold text-slate-900">Foto profil</p>
                  <p class="mt-1 text-sm leading-6 text-slate-500">Gunakan foto yang mudah dikenali anggota tim.</p>
                </div>
              </div>

              <input
                type="file"
                ref="fileInputRef"
                class="hidden"
                accept="image/*"
                @change="handleImageUpload"
              />
            </div>

            <div class="grid gap-5 md:grid-cols-2">
              <div class="space-y-2">
                <Label for="name" class="text-slate-700">Nama Lengkap</Label>
                <div class="relative">
                  <User class="absolute left-3 top-3 h-4 w-4 text-slate-400" />
                  <Input
                    id="name"
                    type="text"
                    placeholder="Nama lengkap Anda"
                    class="rounded-xl border-emerald-100 bg-slate-50 pl-10"
                    v-model="formData.name"
                    required
                  />
                </div>
              </div>

              <div class="space-y-2">
                <Label for="birthdate" class="text-slate-700">Tanggal Lahir</Label>
                <div class="relative">
                  <Calendar class="absolute left-3 top-3 h-4 w-4 text-slate-400" />
                  <Input
                    id="birthdate"
                    type="date"
                    class="rounded-xl border-emerald-100 bg-slate-50 pl-10"
                    v-model="formData.birthdate"
                    required
                  />
                </div>
              </div>
            </div>

            <div class="space-y-2">
              <Label for="role" class="text-slate-700">Role Utama</Label>
              <div class="relative">
                <Briefcase class="absolute left-3 top-3 h-4 w-4 text-slate-400 z-10" />
                <Select v-model="formData.role" placeholder="Pilih role Anda" class="pl-10">
                  <template #default="{ selectOption }">
                    <SelectItem
                      v-for="role in ROLES"
                      :key="role.value"
                      :value="role.value"
                      @select="selectOption(role.value)"
                    >
                      <div class="flex items-center gap-2">
                        <div :class="`h-3 w-3 rounded-full ${role.color}`"></div>
                        {{ role.label }}
                      </div>
                    </SelectItem>
                  </template>
                </Select>
              </div>
            </div>

            <div class="space-y-2">
              <Label for="skills" class="text-slate-700">Skills</Label>
              <div class="flex flex-col gap-2 sm:flex-row">
                <div class="relative flex-1">
                  <Tag class="absolute left-3 top-3 h-4 w-4 text-slate-400" />
                  <Input
                    id="skills"
                    type="text"
                    placeholder="Tambah skill, contoh: Vue, Python, Figma"
                    class="rounded-xl border-emerald-100 bg-slate-50 pl-10"
                    v-model="skillInput"
                    @keypress.enter.prevent="handleAddSkill"
                  />
                </div>
                <Button type="button" variant="outline" class="rounded-xl border-emerald-200 px-5" @click="handleAddSkill">
                  Tambah
                </Button>
              </div>

              <div v-if="formData.skills.length > 0" class="flex flex-wrap gap-2 rounded-2xl border border-emerald-100 bg-emerald-50 p-3">
                <Badge
                  v-for="(skill, index) in formData.skills"
                  :key="index"
                  class="bg-white text-emerald-700"
                >
                  {{ skill }}
                  <button type="button" class="ml-2 hover:text-red-600" @click="handleRemoveSkill(skill)">
                    <X class="h-3 w-3" />
                  </button>
                </Badge>
              </div>
            </div>

            <Button
              type="submit"
              class="h-12 w-full rounded-xl text-base shadow-sm shadow-emerald-200"
              :disabled="loading"
            >
              {{ loading ? 'Menyimpan...' : 'Simpan Profil' }}
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  </div>
</template>
