# http://msdn.microsoft.com/en-us/library/ms681382(VS.85).aspx
ERROR_SUCCESS = 0x0                     # The operation completed successfully.
ERROR_INVALID_FUNCTION = 0x1            # Incorrect function.
ERROR_FILE_NOT_FOUND = 0x2              # The system cannot find the file specified.
ERROR_PATH_NOT_FOUND = 0x3              # The system cannot find the path specified.
ERROR_TOO_MANY_OPEN_FILES = 0x4         # The system cannot open the file.
ERROR_ACCESS_DENIED = 0x5               # Access is denied.
ERROR_INVALID_HANDLE = 0x6              # The handle is invalid.
ERROR_ARENA_TRASHED = 0x7               # The storage control blocks were destroyed.
ERROR_NOT_ENOUGH_MEMORY = 0x8           # Not enough storage is available to process this command.
ERROR_INVALID_BLOCK = 0x9               # The storage control block address is invalid.
ERROR_BAD_ENVIRONMENT = 0xA             # The environment is incorrect.
ERROR_BAD_FORMAT = 0xB                  # An attempt was made to load a program with an incorrect format.
ERROR_INVALID_ACCESS = 0xC              # The access code is invalid.
ERROR_INVALID_DATA = 0xD                # The data is invalid.
ERROR_OUTOFMEMORY = 0xE                 # Not enough storage is available to complete this operation.
ERROR_INVALID_DRIVE = 0xF               # The system cannot find the drive specified.
ERROR_CURRENT_DIRECTORY = 0x10          # The directory cannot be removed.
ERROR_NOT_SAME_DEVICE = 0x11            # The system cannot move the file to a different disk drive.
ERROR_NO_MORE_FILES = 0x12              # There are no more files.
ERROR_WRITE_PROTECT = 0x13              # The media is write protected.
ERROR_BAD_UNIT = 0x14                   # The system cannot find the device specified.
ERROR_NOT_READY = 0x15                  # The device is not ready.
ERROR_BAD_COMMAND = 0x16                # The device does not recognize the command.
ERROR_CRC = 0x17                        # Data error (cyclic redundancy check).
ERROR_BAD_LENGTH = 0x18                 # The program issued a command but the command length is incorrect.
ERROR_SEEK = 0x19                       # The drive cannot locate a specific area or track on the disk.
ERROR_NOT_DOS_DISK = 0x1A               # The specified disk or diskette cannot be accessed.
ERROR_SECTOR_NOT_FOUND = 0x1B           # The drive cannot find the sector requested.
ERROR_OUT_OF_PAPER = 0x1C               # The printer is out of paper.
ERROR_WRITE_FAULT = 0x1D                # The system cannot write to the specified device.
ERROR_READ_FAULT = 0x1E                 # The system cannot read from the specified device.
ERROR_GEN_FAILURE = 0x1F                # A device attached to the system is not functioning.
ERROR_SHARING_VIOLATION = 0x20          # The process cannot access the file because it is being used by another
                                        # process.
ERROR_LOCK_VIOLATION = 0x21             # The process cannot access the file because another process has locked a
                                        # portion of the file.
ERROR_WRONG_DISK = 0x22                 # The wrong diskette is in the drive. Insert %2 (Volume Serial Number: %3)
                                        # into drive %1.
ERROR_SHARING_BUFFER_EXCEEDED = 0x24    # Too many files opened for sharing.
ERROR_HANDLE_EOF = 0x26                 # Reached the end of the file.
ERROR_HANDLE_DISK_FULL = 0x27           # The disk is full.
ERROR_NOT_SUPPORTED = 0x32              # The request is not supported.
ERROR_REM_NOT_LIST = 0x33               # Windows cannot find the network path. Verify that the network path is
                                        # correct and the destination computer is not busy or turned off. If Windows
                                        # still cannot find the network path, contact your network administrator.
ERROR_DUP_NAME = 0x34                   # You were not connected because a duplicate name exists on the network. If
                                        # joining a domain, go to System in Control Panel to change the computer name
                                        # and try again. If joining a workgroup, choose another workgroup name.
ERROR_BAD_NETPATH = 0x35                # The network path was not found.
ERROR_NETWORK_BUSY = 0x36               # The network is busy.
ERROR_DEV_NOT_EXIST = 0x37              # The specified network resource or device is no longer available.
ERROR_TOO_MANY_CMDS = 0x38              # The network BIOS command limit has been reached.
ERROR_ADAP_HDW_ERR = 0x39               # A network adapter hardware error occurred.
ERROR_BAD_NET_RESP = 0x3A               # The specified server cannot perform the requested operation.
ERROR_UNEXP_NET_ERR = 0x3B              # An unexpected network error occurred.
ERROR_BAD_REM_ADAP = 0x3C               # The remote adapter is not compatible.
ERROR_PRINTQ_FULL = 0x3D                # The printer queue is full.
ERROR_NO_SPOOL_SPACE = 0x3E             # Space to store the file waiting to be printed is not available on the server.
ERROR_PRINT_CANCELLED = 0x3F            # Your file waiting to be printed was deleted.
ERROR_NETNAME_DELETED = 0x40            # The specified network name is no longer available.
ERROR_NETWORK_ACCESS_DENIED = 0x41      # Network access is denied.
ERROR_BAD_DEV_TYPE = 0x42               # The network resource type is not correct.
ERROR_BAD_NET_NAME = 0x43               # The network name cannot be found.
ERROR_TOO_MANY_NAMES = 0x44             # The name limit for the local computer network adapter card was exceeded.
ERROR_TOO_MANY_SESS = 0x45              # The network BIOS session limit was exceeded.
ERROR_SHARING_PAUSED = 0x46             # The remote server has been paused or is in the process of being started.
ERROR_REQ_NOT_ACCEP = 0x47              # No more connections can be made to this remote computer at this time because
                                        # there are already as many connections as the computer can accept.
ERROR_REDIR_PAUSED = 0x48               # The specified printer or disk device has been paused.
ERROR_FILE_EXISTS = 0x50                # The file exists.
ERROR_CANNOT_MAKE = 0x52                # The directory or file cannot be created.
ERROR_FAIL_I24 = 0x53                   # Fail on INT 24.
ERROR_OUT_OF_STRUCTURES = 0x54          # Storage to process this request is not available.
ERROR_ALREADY_ASSIGNED = 0x55           # The local device name is already in use.
ERROR_INVALID_PASSWORD = 0x56           # The specified network password is not correct.
ERROR_INVALID_PARAMETER = 0x57          # The parameter is incorrect.
ERROR_NET_WRITE_FAULT = 0x58            # A write fault occurred on the network.
ERROR_NO_PROC_SLOTS = 0x59              # The system cannot start another process at this time.
ERROR_TOO_MANY_SEMAPHORES = 0x64        # Cannot create another system semaphore.
ERROR_EXCL_SEM_ALREADY_OWNED = 0x65     # The exclusive semaphore is owned by another process.
ERROR_SEM_IS_SET = 0x66                 # The semaphore is set and cannot be closed.
ERROR_TOO_MANY_SEM_REQUESTS = 0x67      # The semaphore cannot be set again.
ERROR_INVALID_AT_INTERRUPT_TIME = 0x68  # Cannot request exclusive semaphores at interrupt time.
ERROR_SEM_OWNER_DIED = 0x69             # The previous ownership of this semaphore has ended.
ERROR_SEM_USER_LIMIT = 0x6A             # Insert the diskette for drive %1.
ERROR_DISK_CHANGE = 0x6B                # The program stopped because an alternate diskette was not inserted.
ERROR_DRIVE_LOCKED = 0x6C               # The disk is in use or locked by another process.
ERROR_BROKEN_PIPE = 0x6D                # The pipe has been ended.
ERROR_OPEN_FAILED = 0x6E                # The system cannot open the device or file specified.
ERROR_BUFFER_OVERFLOW = 0x6F            # The file name is too long.
ERROR_DISK_FULL = 0x70                  # There is not enough space on the disk.
ERROR_NO_MORE_SEARCH_HANDLES = 0x71     # No more internal file identifiers available.
ERROR_INVALID_TARGET_HANDLE = 0x72      # The target internal file identifier is incorrect.
ERROR_INVALID_CATEGORY = 0x75           # The IOCTL call made by the application program is not correct.
ERROR_INVALID_VERIFY_SWITCH = 0x76      # The verify-on-write switch parameter value is not correct.
ERROR_BAD_DRIVER_LEVEL = 0x77           # The system does not support the command requested.
ERROR_CALL_NOT_IMPLEMENTED = 0x78       # This function is not supported on this system.
ERROR_SEM_TIMEOUT = 0x79                # The semaphore timeout period has expired.
ERROR_INSUFFICIENT_BUFFER = 0x7A        # The data area passed to a system call is too small.
ERROR_INVALID_NAME = 0x7B               # The filename, directory name, or volume label syntax is incorrect.
ERROR_INVALID_LEVEL = 0x7C              # The system call level is not correct.
ERROR_NO_VOLUME_LABEL = 0x7D            # The disk has no volume label.
ERROR_MOD_NOT_FOUND = 0x7E              # The specified module could not be found.
ERROR_PROC_NOT_FOUND = 0x7F             # The specified procedure could not be found.
ERROR_WAIT_NO_CHILDREN = 0x80           # There are no child processes to wait for.
ERROR_CHILD_NOT_COMPLETE = 0x81         # The %1 application cannot be run in Win32 mode.
ERROR_DIRECT_ACCESS_HANDLE = 0x82       # Attempt to use a file handle to an open disk partition for an operation other
                                        # than raw disk I/O.
ERROR_NEGATIVE_SEEK = 0x83              # An attempt was made to move the file pointer before the beginning of the file.
ERROR_SEEK_ON_DEVICE = 0x84             # The file pointer cannot be set on the specified device or file.
ERROR_IS_JOIN_TARGET = 0x85             # A JOIN or SUBST command cannot be used for a drive that contains previously
                                        # joined drives.
ERROR_IS_JOINED = 0x86                  # An attempt was made to use a JOIN or SUBST command on a drive that has
                                        # already been joined.
ERROR_IS_SUBSTED = 0x87                 # An attempt was made to use a JOIN or SUBST command on a drive that has
                                        # already been substituted.
ERROR_NOT_JOINED = 0x88                 # The system tried to delete the JOIN of a drive that is not joined.
ERROR_NOT_SUBSTED = 0x89                # The system tried to delete the substitution of a drive that is not
                                        # substituted.
ERROR_JOIN_TO_JOIN = 0x8A               # The system tried to join a drive to a directory on a joined drive.
ERROR_SUBST_TO_SUBST = 0x8B             # The system tried to substitute a drive to a directory on a substituted drive.
ERROR_JOIN_TO_SUBST = 0x8C              # The system tried to join a drive to a directory on a substituted drive.
ERROR_SUBST_TO_JOIN = 0x8D              # The system tried to SUBST a drive to a directory on a joined drive.
ERROR_BUSY_DRIVE = 0x8E                 # The system cannot perform a JOIN or SUBST at this time.
ERROR_SAME_DRIVE = 0x8F                 # The system cannot join or substitute a drive to or for a directory on the
                                        # same drive.
ERROR_DIR_NOT_ROOT = 0x90               # The directory is not a subdirectory of the root directory.
ERROR_DIR_NOT_EMPTY = 0x91              # The directory is not empty.
ERROR_IS_SUBST_PATH = 0x92              # The path specified is being used in a substitute.
ERROR_IS_JOIN_PATH = 0x93               # Not enough resources are available to process this command.
ERROR_PATH_BUSY = 0x94                  # The path specified cannot be used at this time.
ERROR_IS_SUBST_TARGET = 0x95            # An attempt was made to join or substitute a drive for which a directory on
                                        # the drive is the target of a previous substitute.
ERROR_SYSTEM_TRACE = 0x96               # System trace information was not specified in your CONFIG.SYS file, or
                                        # tracing is disallowed.
ERROR_INVALID_EVENT_COUNT = 0x97        # The number of specified semaphore events for DosMuxSemWait is not correct.
ERROR_TOO_MANY_MUXWAITERS = 0x98        # DosMuxSemWait did not execute; too many semaphores are already set.
ERROR_INVALID_LIST_FORMAT = 0x99        # The DosMuxSemWait list is not correct.
ERROR_LABEL_TOO_LONG = 0x9A             # The volume label you entered exceeds the label character limit of the target
                                        # file system.
ERROR_TOO_MANY_TCBS = 0x9B              # Cannot create another thread.
ERROR_SIGNAL_REFUSED = 0x9C             # The recipient process has refused the signal.
ERROR_DISCARDED = 0x9D                  # The segment is already discarded and cannot be locked.
ERROR_NOT_LOCKED = 0x9E                 # The segment is already unlocked.
ERROR_BAD_THREADID_ADDR = 0x9F          # The address for the thread ID is not correct.
ERROR_BAD_ARGUMENTS = 0xA0              # One or more arguments are not correct.
ERROR_BAD_PATHNAME = 0xA1               # The specified path is invalid.
ERROR_SIGNAL_PENDING = 0xA2             # A signal is already pending.
ERROR_MAX_THRDS_REACHED = 0xA4          # No more threads can be created in the system.
ERROR_LOCK_FAILED = 0xA7                # Unable to lock a region of a file.
ERROR_BUSY = 0xAA                       # The requested resource is in use.
ERROR_CANCEL_VIOLATION = 0xAD           # A lock request was not outstanding for the supplied cancel region.
ERROR_ATOMIC_LOCKS_NOT_SUPPORTED = 0xAE # The file system does not support atomic changes to the lock type.
ERROR_INVALID_SEGMENT_NUMBER = 0xB4     # The system detected a segment number that was not correct.
ERROR_INVALID_ORDINAL = 0xB6            # The operating system cannot run %1.
ERROR_ALREADY_EXISTS = 0xB7             # Cannot create a file when that file already exists.
ERROR_INVALID_FLAG_NUMBER = 0xBA        # The flag passed is not correct.
ERROR_SEM_NOT_FOUND = 0xBB              # The specified system semaphore name was not found.
ERROR_INVALID_STARTING_CODESEG = 0xBC   # The operating system cannot run %1.
ERROR_INVALID_STACKSEG = 0xBD           # The operating system cannot run %1.
ERROR_INVALID_MODULETYPE = 0xBE         # The operating system cannot run %1.
ERROR_INVALID_EXE_SIGNATURE = 0xBF      # Cannot run %1 in Win32 mode.
ERROR_EXE_MARKED_INVALID = 0xC0         # The operating system cannot run %1.
ERROR_BAD_EXE_FORMAT = 0xC1             # %1 is not a valid Win32 application.
ERROR_ITERATED_DATA_EXCEEDS_64k = 0xC2  # The operating system cannot run %1.
ERROR_INVALID_MINALLOCSIZE = 0xC3       # The operating system cannot run %1.
ERROR_DYNLINK_FROM_INVALID_RING = 0xC4  # The operating system cannot run this application program.
ERROR_IOPL_NOT_ENABLED = 0xC5           # The operating system is not presently configured to run this application.
ERROR_INVALID_SEGDPL = 0xC6             # The operating system cannot run %1.
ERROR_AUTODATASEG_EXCEEDS_64k = 0xC7    # The operating system cannot run this application program.
ERROR_RING2SEG_MUST_BE_MOVABLE = 0xC8   # The code segment cannot be greater than or equal to 64K.
ERROR_RELOC_CHAIN_XEEDS_SEGLIM = 0xC9   # The operating system cannot run %1.
ERROR_INFLOOP_IN_RELOC_CHAIN = 0xCA     # The operating system cannot run %1.
ERROR_ENVVAR_NOT_FOUND = 0xCB           # The system could not find the environment option that was entered.
ERROR_NO_SIGNAL_SENT = 0xCD             # No process in the command subtree has a signal handler.
ERROR_FILENAME_EXCED_RANGE = 0xCE       # The filename or extension is too long.
ERROR_RING2_STACK_IN_USE = 0xCF         # The ring 2 stack is in use.
ERROR_META_EXPANSION_TOO_LONG = 0xD0    # The global filename characters, * or ?, are entered incorrectly or too many
                                        # global filename characters are specified.
ERROR_INVALID_SIGNAL_NUMBER = 0xD1      # The signal being posted is not correct.
ERROR_THREAD_1_INACTIVE = 0xD2          # The signal handler cannot be set.
ERROR_LOCKED = 0xD4                     # The segment is locked and cannot be reallocated.
ERROR_TOO_MANY_MODULES = 0xD6           # Too many dynamic-link modules are attached to this program or dynamic-link
                                        # module.
ERROR_NESTING_NOT_ALLOWED = 0xD7        # Cannot nest calls to LoadModule.
ERROR_EXE_MACHINE_TYPE_MISMATCH = 0xD8  # The version of %1 is not compatible with the version you're running. Check
                                        # your computer's system information to see whether you need a x86 (32-bit) or
                                        # x64 (64-bit) version of the program, and then contact the software publisher.
ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY = 0xD9 # The image file %1 is signed, unable to modify.
ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY = 0xDA # The image file %1 is strong signed, unable to modify.
ERROR_FILE_CHECKED_OUT = 0xDC           # This file is checked out or locked for editing by another user.
ERROR_CHECKOUT_REQUIRED = 0xDD          # The file must be checked out before saving changes.
ERROR_BAD_FILE_TYPE = 0xDE              # The file type being saved or retrieved has been blocked.
ERROR_FILE_TOO_LARGE = 0xDF             # The file size exceeds the limit allowed and cannot be saved.
ERROR_FORMS_AUTH_REQUIRED = 0xE0        # Access Denied. Before opening files in this location, you must first add the
                                        # web site to your trusted sites list, browse to the web site, and select the
                                        # option to login automatically.
ERROR_VIRUS_INFECTED = 0xE1             # Operation did not complete successfully because the file contains a virus.
ERROR_VIRUS_DELETED = 0xE2              # This file contains a virus and cannot be opened. Due to the nature of this
                                        # virus, the file has been removed from this location.
ERROR_PIPE_LOCAL = 0xE5                 # The pipe is local.
ERROR_BAD_PIPE = 0xE6                   # The pipe state is invalid.
ERROR_PIPE_BUSY = 0xE7                  # All pipe instances are busy.
ERROR_NO_DATA = 0xE8                    # The pipe is being closed.
ERROR_PIPE_NOT_CONNECTED = 0xE9         # No process is on the other end of the pipe.
ERROR_MORE_DATA = 0xEA                  # More data is available.
ERROR_VC_DISCONNECTED = 0xF0            # The session was canceled.
ERROR_INVALID_EA_NAME = 0xFE            # The specified extended attribute name was invalid.
ERROR_EA_LIST_INCONSISTENT = 0xFF       # The extended attributes are inconsistent.
WAIT_TIMEOUT = 0x102                    # The wait operation timed out.
ERROR_NO_MORE_ITEMS = 0x103             # No more data is available.
ERROR_CANNOT_COPY = 0x10A               # The copy functions cannot be used.
ERROR_DIRECTORY = 0x10B                 # The directory name is invalid.
ERROR_EAS_DIDNT_FIT = 0x113             # The extended attributes did not fit in the buffer.
ERROR_EA_FILE_CORRUPT = 0x114           # The extended attribute file on the mounted file system is corrupt.
ERROR_EA_TABLE_FULL = 0x115             # The extended attribute table file is full.
ERROR_INVALID_EA_HANDLE = 0x116         # The specified extended attribute handle is invalid.
ERROR_EAS_NOT_SUPPORTED = 0x11A         # The mounted file system does not support extended attributes.
ERROR_NOT_OWNER = 0x120                 # Attempt to release mutex not owned by caller.
ERROR_TOO_MANY_POSTS = 0x12A            # Too many posts were made to a semaphore.
ERROR_PARTIAL_COPY = 0x12B              # Only part of a ReadProcessMemory or WriteProcessMemory request was completed.
ERROR_OPLOCK_NOT_GRANTED = 0x12C        # The oplock request is denied.
ERROR_INVALID_OPLOCK_PROTOCOL = 0x12D   # An invalid oplock acknowledgment was received by the system.
ERROR_DISK_TOO_FRAGMENTED = 0x12E       # The volume is too fragmented to complete this operation.
ERROR_DELETE_PENDING = 0x12F            # The file cannot be opened because it is in the process of being deleted.
ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING = 0x130 # Short name settings may not be changed on this
                                        # volume due to the global registry setting.
ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME = 0x131 # Short names are not enabled on this volume.
ERROR_SECURITY_STREAM_IS_INCONSISTENT = 0x132 # The security stream for the given volume is in an inconsistent state.
                                        # Please run CHKDSK on the volume.
ERROR_INVALID_LOCK_RANGE = 0x133        # A requested file lock operation cannot be processed due to an invalid byte
                                        # range.
ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT = 0x134 # The subsystem needed to support the image type is not present.
ERROR_NOTIFICATION_GUID_ALREADY_DEFINED = 0x135 # The specified file already has a notification GUID associated with it.
ERROR_MR_MID_NOT_FOUND = 0x13D          # The system cannot find message text for message number 0x%1 in the message
                                        # file for %2.
ERROR_SCOPE_NOT_FOUND = 0x13E           # The scope specified was not found.
ERROR_FAIL_NOACTION_REBOOT = 0x15E      # No action was taken as a system reboot is required.
ERROR_FAIL_SHUTDOWN = 0x15F             # The shutdown operation failed.
ERROR_FAIL_RESTART = 0x160              # The restart operation failed.
ERROR_MAX_SESSIONS_REACHED = 0x161      # The maximum number of sessions has been reached.
ERROR_THREAD_MODE_ALREADY_BACKGROUND = 0x190 # The thread is already in background processing mode.
ERROR_THREAD_MODE_NOT_BACKGROUND = 0x191 # The thread is not in background processing mode.
ERROR_PROCESS_MODE_ALREADY_BACKGROUND = 0x192 # The process is already in background processing mode.
ERROR_PROCESS_MODE_NOT_BACKGROUND = 0x193 # The process is not in background processing mode.
ERROR_INVALID_ADDRESS = 0x1E7           # Attempt to access invalid address.
# TODO: Add remaining errors