#
# PySNMP MIB module VELOCLOUD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VELOCLOUD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:15:40 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, IpAddress, Integer32, MibIdentifier, TimeTicks, iso, Gauge32, enterprises, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "IpAddress", "Integer32", "MibIdentifier", "TimeTicks", "iso", "Gauge32", "enterprises", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
velocloud = ModuleIdentity((1, 3, 6, 1, 4, 1, 45346))
velocloud.setRevisions(('2021-05-11 00:00', '2019-08-02 00:00', '2017-01-18 00:00', '2017-01-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: velocloud.setRevisionsDescriptions(('Update of VMware nomenclature', 'Implementation of VMware SD-WAN Edge MIB Objects', 'Implementation of VCO MIB Objects', 'Inital definition of VMware SD-WAN MIB Objects',))
if mibBuilder.loadTexts: velocloud.setLastUpdated('202105110000Z')
if mibBuilder.loadTexts: velocloud.setOrganization('VMware Corporation')
if mibBuilder.loadTexts: velocloud.setContactInfo('postal:    VMware Corporation \n                                    World Headquarters\n                                    3401 Hillview Avenue\n                                    Palo Alto, CA 943043\n                                    USA\n                        \n                         web:       sase.vmware.com')
if mibBuilder.loadTexts: velocloud.setDescription('Top-level infrastructure of the VMware SD-WAN enterprise MIB tree')
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 45346, 1))
mibBuilder.exportSymbols("VELOCLOUD-MIB", velocloud=velocloud, modules=modules, PYSNMP_MODULE_ID=velocloud)
