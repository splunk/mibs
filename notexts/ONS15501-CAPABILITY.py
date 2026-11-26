#
# PySNMP MIB module ONS15501-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/ONS15501-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
synchronous, = mibBuilder.importSymbols("ONS15501-MIB", "synchronous")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ons15501MIBCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 1869, 15, 11))
ons15501MIBCapabilities.setRevisions(('2002-10-15 18:00',))
if mibBuilder.loadTexts: ons15501MIBCapabilities.setLastUpdated('200210151800Z')
if mibBuilder.loadTexts: ons15501MIBCapabilities.setOrganization('Cisco Systems, Inc.')
synEmbLxCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 1869, 15))
ons15501CapOld = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setProductRelease('Release 3.0 of ONS15501 software.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapOld = ons15501CapOld.setStatus('current')
ons15501CapDC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setProductRelease('DC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapDC = ons15501CapDC.setStatus('current')
ons15501CapAC = AgentCapabilities((1, 3, 6, 1, 4, 1, 1869, 15, 11, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setProductRelease('AC series of ONS15501, Release 4.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ons15501CapAC = ons15501CapAC.setStatus('current')
mibBuilder.exportSymbols("ONS15501-CAPABILITY", ons15501MIBCapabilities=ons15501MIBCapabilities, PYSNMP_MODULE_ID=ons15501MIBCapabilities, ons15501CapOld=ons15501CapOld, ons15501CapAC=ons15501CapAC, synEmbLxCapability=synEmbLxCapability, ons15501CapDC=ons15501CapDC)
