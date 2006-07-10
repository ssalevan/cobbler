"""
Messages used by cobbler.
This module encapsulates strings so they can
be reused and potentially translated.

Copyright 2006, Red Hat, Inc
Michael DeHaan <mdehaan@redhat.com>

This software may be freely redistributed under the terms of the GNU
general public license.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""

_msg_table = {
  "bad_server"      : "The 'server' field in /var/lib/cobbler/settings must be set to something other than localhost, or kickstarting features will not work",
  "parse_error"     : "cobbler could not read %s, replacing...",
  "no_create"       : "cobbler could not create: %s",
  "no_delete"       : "cobbler could not delete: %s",
  "no_args"         : "this command requires arguments.",
  "missing_options" : "cannot perform this action, more arguments are required",
  "unknown_cmd"     : "cobbler doesn't understand '%s'",
  "bad_arg"         : "cobbler was expecting an equal sign in argument '%s'",
  "reject_arg"      : "the value of parameter '%s' isn't valid",
  "weird_arg"       : "this command doesn't take a parameter named '%s'",
  "bad_sys_name"    : "system name must be a MAC, IP, or resolveable host",
  "usage"           : "for help, see 'man cobbler'",
  "need_to_fix"     : "the following potential problems were detected:",
  "need_perms"      : "cobbler could not access %s",
  "need_perms2"     : "cobbler could not copy %s to %s",
  "no_dhcpd"        : "cobbler couldn't find dhcpd, try 'yum install dhcpd'",
  "no_pxelinux"     : "cobbler couldn't find pxelinux, try 'yum install pxelinux'",
  "no_tftpd"        : "cobbler couldn't find tftpd, try 'yum install tftpd'",
  "no_dir"          : "cobbler couldn't find %s, please create it",
  "chg_attrib"      : "need to change field '%s' value to '%s' in file '%s'",
  "no_exist"        : "file %s does not exist",
  "no_line"         : "file '%s' should have a line '%s' somewhere",
  "no_dir2"         : "can't find %s for %s as referenced in /var/lib/cobbler/settings",
  "bad_param"       : "at least one parameter is missing for this function",
  "empty_list"      : "There are no configured items.",
  "err_resolv"      : "The system name (%s) did not resolve",
  "err_kickstart"   : "The kickstart (%s) for item (%s) is not valid",
  "err_kickstart2"  : "Error while mirroring kickstart file (%s) to (%s)",
  "orphan_profile"  : "Removing this system would break profile '%s'",
  "orphan_profile2" : "system (%s) references a non-existant profile (%s)",
  "orphan_distro2"  : "profile (%s) references a non-existant distro (%s)",
  "orphan_system"   : "Removing this profile would break system '%s'",
  "delete_nothing"  : "can't delete something that doesn't exist",
  "no_distro"       : "distro does not exist",
  "no_profile"      : "profile does not exist",
  "no_kickstart"    : "kickstart must be an absolute path, or an http://, ftp:// or nfs:// URL",
  "no_kernel"       : "the kernel needs to be a directory containing a kernel, or a full path.  Kernels must be named just 'vmlinuz' or in the form 'vmlinuz-AA.BB.CC-something'",
  "sync_kernel"     : "the kernel (%s) for distro (%s) cannot be found and must be fixed",
  "sync_initrd"     : "the initrd (%s) for distro (%s) cannot be found and must be fixed",
  "sync_mirror_ks"  : "mirroring local kickstarts...",
  "sync_buildtree"  : "building trees",
  "sync_processing" : "processing: %s",
  "writing"         : "writing file: %s",
  "mkdir"           : "creating: %s",
  "dryrun"          : "dry run | %s",
  "copying"         : "copying file: %s to %s",
  "removing"        : "removing: %s",
  "no_initrd"       : "the initrd needs to be a directory containing an initrd, or a full path.  Initrds must be named just 'initrd.img' or in the form 'initrd-AA.BB.CC-something.img",
  "exc_xen_name"    : "invalid Xen name",
  "exc_xen_file"    : "invalid Xen file size",
  "exc_xen_mac"     : "invalid Xen mac address",
  "exc_xen_para"    : "invalid Xen paravirtualization setting",
  "exc_profile"     : "invalid profile name",
  "exc_profile2"    : "profile name not set",
  "check_ok"        : """
No setup problems found.

Manual editing of /var/lib/cobbler/settings and dhcpd.conf is suggested to tailor them to your specific configuration.  Furthermore, it's important to know that cobbler can't completely understnad what you intend to do with dhcpd.conf, but it looks like there is at least some PXE related information in it.  We'll leave this up to you.

Good luck.
""",
  "help"           : "see 'man cobbler'"
}

def lookup(key):
   """
   Return the lookup of a string key.
   """
   if _msg_table.has_key(key):
       return _msg_table[key]
   return key