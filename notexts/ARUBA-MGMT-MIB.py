#
# PySNMP MIB module ARUBA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/ARUBA-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
arubaMgmt, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMgmt")
ArubaEnableValue, = mibBuilder.importSymbols("ARUBA-TC", "ArubaEnableValue")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Bits, ObjectName, Gauge32, TimeTicks, ModuleIdentity, snmpModules, MibIdentifier, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Bits", "ObjectName", "Gauge32", "TimeTicks", "ModuleIdentity", "snmpModules", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType")
DisplayString, TestAndIncr, TimeStamp, PhysAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TimeStamp", "PhysAddress", "TextualConvention", "TruthValue")
arubaMgmtExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 3, 3))
if mibBuilder.loadTexts: arubaMgmtExtensions.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: arubaMgmtExtensions.setOrganization('Aruba, a Hewlett Packard Enterprise company')
arubaMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1))
arubaGetTable = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: arubaGetTable.setStatus('current')
arubaNumberOfRows = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: arubaNumberOfRows.setStatus('current')
arubaRowInstance = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arubaRowInstance.setStatus('current')
arubaGetTableStatus = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("endTable", 1), ("moreTable", 2), ("retrieveError", 3), ("noAmpSupport", 4), ("invalidColumnID", 5), ("resourceAllocationFailure", 6))))
if mibBuilder.loadTexts: arubaGetTableStatus.setStatus('current')
arubaNumberOfColumns = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: arubaNumberOfColumns.setStatus('current')
arubaSwitchAMPSupport = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 6), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaSwitchAMPSupport.setStatus('current')
mibBuilder.exportSymbols("ARUBA-MGMT-MIB", arubaNumberOfRows=arubaNumberOfRows, arubaRowInstance=arubaRowInstance, arubaMgmtExtensions=arubaMgmtExtensions, arubaSwitchAMPSupport=arubaSwitchAMPSupport, arubaGetTable=arubaGetTable, arubaGetTableStatus=arubaGetTableStatus, arubaMgmtGroup=arubaMgmtGroup, PYSNMP_MODULE_ID=arubaMgmtExtensions, arubaNumberOfColumns=arubaNumberOfColumns)
