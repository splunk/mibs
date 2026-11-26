#
# PySNMP MIB module CISCO-DMN-DSG-LOCKLEVEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-LOCKLEVEL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGLockLevel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22))
ciscoDSGLockLevel.setRevisions(('2010-08-30 11:00', '2010-06-28 06:00', '2010-05-24 06:30', '2009-12-20 12:00',))
if mibBuilder.loadTexts: ciscoDSGLockLevel.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setOrganization('Cisco Systems, Inc.')
lockLevel = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevel.setStatus('current')
lockLevelPWD = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWD.setStatus('current')
lockLevelPWDCUR = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCUR.setStatus('current')
lockLevelPWDNEW = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDNEW.setStatus('current')
lockLevelPWDCONF = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCONF.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-LOCKLEVEL-MIB", ciscoDSGLockLevel=ciscoDSGLockLevel, lockLevelPWDCUR=lockLevelPWDCUR, lockLevelPWD=lockLevelPWD, lockLevelPWDNEW=lockLevelPWDNEW, lockLevel=lockLevel, lockLevelPWDCONF=lockLevelPWDCONF, PYSNMP_MODULE_ID=ciscoDSGLockLevel)
