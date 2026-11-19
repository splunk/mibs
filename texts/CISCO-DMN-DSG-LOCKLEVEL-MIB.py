#
# PySNMP MIB module CISCO-DMN-DSG-LOCKLEVEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-LOCKLEVEL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGLockLevel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22))
ciscoDSGLockLevel.setRevisions(('2010-08-30 11:00', '2010-06-28 06:00', '2010-05-24 06:30', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGLockLevel.setRevisionsDescriptions(('V01.00.03 2010-08-30\n                   Updated for adherence to SNMPv2 format.', 'V01.00.02 2010-06-28\n                   Updated the description for lockLevel.', 'V01.00.01 2010-05-24\n                   Updated the options for lockLevel.', 'V01.00.00 2009-12-20\n                   Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGLockLevel.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setContactInfo('Cisco Systems, Inc.\n        Customer Service\n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA\n        Tel: +1 800 553 NETS\n\n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setDescription('Cisco Lock Level MIB.')
lockLevel = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevel.setStatus('current')
if mibBuilder.loadTexts: lockLevel.setDescription('Lock Level.\n          (0)   : All settings are unlocked.\n          (1)   : All settings are unlocked except Factory reset,\n                    IP settings and passwords.\n          (2)   : All settings are unlocked except that presets,\n                    tuning related items, and\n                    dish setup are also locked.\n          (3)   : All settings are locked except volume change.\n          (4)   : All settings are locked (can be changed via \n                    NC uplink signal only).\n         four is a read-only value.')
lockLevelPWD = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWD.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWD.setDescription('Password to change Password and Lock Level.')
lockLevelPWDCUR = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCUR.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDCUR.setDescription('Confirm the Current Password.')
lockLevelPWDNEW = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDNEW.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDNEW.setDescription('New Password.')
lockLevelPWDCONF = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCONF.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDCONF.setDescription('Confirm New Password.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-LOCKLEVEL-MIB", ciscoDSGLockLevel=ciscoDSGLockLevel, lockLevelPWD=lockLevelPWD, lockLevelPWDCUR=lockLevelPWDCUR, PYSNMP_MODULE_ID=ciscoDSGLockLevel, lockLevelPWDNEW=lockLevelPWDNEW, lockLevelPWDCONF=lockLevelPWDCONF, lockLevel=lockLevel)
