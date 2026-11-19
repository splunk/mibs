#
# PySNMP MIB module CISCO-COPS-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-COPS-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCopsClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 313))
ciscoCopsClientCapability.setRevisions(('2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCopsClientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCopsClientCapability.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoCopsClientCapability.setDescription('The capabilities description of\n                CISCO-COPS-CLIENT-MIB.')
ccopsClientCapCatOSV53R2Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setProductRelease('Cisco CatOS 5.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV53R2Cat6k = ccopsClientCapCatOSV53R2Cat6k.setStatus('current')
if mibBuilder.loadTexts: ccopsClientCapCatOSV53R2Cat6k.setDescription('CISCO-COPS-CLIENT-MIB capabilities.')
ccopsClientCapCatOSV61R1Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 313, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setProductRelease('Cisco CatOS 6.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccopsClientCapCatOSV61R1Cat6k = ccopsClientCapCatOSV61R1Cat6k.setStatus('current')
if mibBuilder.loadTexts: ccopsClientCapCatOSV61R1Cat6k.setDescription('CISCO-COPS-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-COPS-CLIENT-CAPABILITY", ccopsClientCapCatOSV61R1Cat6k=ccopsClientCapCatOSV61R1Cat6k, ccopsClientCapCatOSV53R2Cat6k=ccopsClientCapCatOSV53R2Cat6k, ciscoCopsClientCapability=ciscoCopsClientCapability, PYSNMP_MODULE_ID=ciscoCopsClientCapability)
