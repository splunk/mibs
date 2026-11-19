#
# PySNMP MIB module CISCO-DS0BUNDLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS0BUNDLE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, TestAndIncr, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "DisplayString", "RowStatus")
ds0Bundle = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 32))
if mibBuilder.loadTexts: ds0Bundle.setLastUpdated('9805242010Z')
if mibBuilder.loadTexts: ds0Bundle.setOrganization('Cisco Systems, Inc.')
dsx0BundleNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 32, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx0BundleNextIndex.setStatus('current')
dsx0BundleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 32, 3), )
if mibBuilder.loadTexts: dsx0BundleTable.setStatus('current')
dsx0BundleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1), ).setIndexNames((0, "CISCO-DS0BUNDLE-MIB", "dsx0BundleIndex"))
if mibBuilder.loadTexts: dsx0BundleEntry.setStatus('current')
dsx0BundleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: dsx0BundleIndex.setStatus('current')
dsx0BundleIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx0BundleIfIndex.setStatus('current')
dsx0BundleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 32, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dsx0BundleRowStatus.setStatus('current')
ds0BundleConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4))
ds0BundleGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1))
ds0BundleCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2))
ds0BundleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 2, 1)).setObjects(("CISCO-DS0BUNDLE-MIB", "ds0BundleConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleCompliance = ds0BundleCompliance.setStatus('current')
ds0BundleConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 32, 4, 1, 2)).setObjects(("CISCO-DS0BUNDLE-MIB", "dsx0BundleNextIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleIfIndex"), ("CISCO-DS0BUNDLE-MIB", "dsx0BundleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ds0BundleConfigGroup = ds0BundleConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-MIB", dsx0BundleTable=dsx0BundleTable, dsx0BundleEntry=dsx0BundleEntry, ds0BundleCompliances=ds0BundleCompliances, PYSNMP_MODULE_ID=ds0Bundle, dsx0BundleIndex=dsx0BundleIndex, dsx0BundleIfIndex=dsx0BundleIfIndex, dsx0BundleNextIndex=dsx0BundleNextIndex, ds0BundleCompliance=ds0BundleCompliance, dsx0BundleRowStatus=dsx0BundleRowStatus, ds0BundleGroups=ds0BundleGroups, ds0BundleConformance=ds0BundleConformance, ds0BundleConfigGroup=ds0BundleConfigGroup, ds0Bundle=ds0Bundle)
