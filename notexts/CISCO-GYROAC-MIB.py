#
# PySNMP MIB module CISCO-GYROAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GYROAC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGyroacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 859))
ciscoGyroacMIB.setRevisions(('2019-01-09 00:00',))
if mibBuilder.loadTexts: ciscoGyroacMIB.setLastUpdated('201901090000Z')
if mibBuilder.loadTexts: ciscoGyroacMIB.setOrganization('Cisco Systems, Inc.')
ciscoGyroacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 859, 0))
ciscoGyro = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 859, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoGyro.setStatus('current')
mibBuilder.exportSymbols("CISCO-GYROAC-MIB", ciscoGyroacMIB=ciscoGyroacMIB, PYSNMP_MODULE_ID=ciscoGyroacMIB, ciscoGyroacMIBObjects=ciscoGyroacMIBObjects, ciscoGyro=ciscoGyro)
